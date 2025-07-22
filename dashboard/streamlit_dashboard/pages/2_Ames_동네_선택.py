import streamlit as st
import pandas as pd
import numpy as np
import os

# 데이터 불러오기
eda_df = pd.read_csv('data/eda_house.csv')
score_df = pd.read_csv('data/score_house.csv')


# 페이지 설정
st.set_page_config(page_title="Ames 동네 선택", page_icon="📌", layout="wide")

st.title("📌 Ames 동네 선택")

st.write('---')

col1, col2 = st.columns(2)

with col1:
    st.subheader('학교와 병원이 밀집되어 있는 3곳 선정')
    st.write('학교와 병원이 밀집되어 있는 곳에서 조건에 맞는 주택 찾기')
    with st.expander('중요하게 생각하는 요소'):
        st.write('''
        \- 주택 근처에 학교와 병원이 밀집되어 있는가.
        \n \- 주택의 전반적인 상태 평가가 좋은가.
        \n \- 주택의 외관 자재의 현재 상태 평가가 좋은가.
        \n \- 주택의 지상 거주 면적이 넓은가.
        \n \- 주택의 지상 침실 수가 많은가.
        \n \- 주택의 지상 층의 총 방 개수 (욕실 제외)가 많은가.
        \n \- 주택의 차량 수용 능력이 좋은가.
        \n \- 주택의 진입로 포장 상태가 전면 포장인가.
        \n \- 주택의 울타리가 적어도 최소한의 프라이버시 울타리인가.
        \n \- 주택의 건축 연도 혹은 리모델링 연도가 최근인가.
            ''')
        
    st.write('빨간색 : 군집0 , 파란색 : 군집1, 보라색 : 군집2')

with col2:
    with open("dashboard/img/select_cluster_map.html", "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=300, scrolling=False)


st.write('')
st.write('')
st.write('')

# --------------------------------- streamlit
st.write('### [streamlit 시각화] 사이드바 버튼 상호작용 그래프')
st.write('''
streamlit 그래프로 알아보기 - 사이드 바에서 군집과 관심 주제를 설정하세요.
\n해당 그래프는 설정한 조건의 가구 수를 알아보는 그래프입니다.
''')
st.write('초기 설정 : 군집 0 의 침실 수 막대 그래프')

select0 = st.sidebar.checkbox('군집0')
select1 = st.sidebar.checkbox('군집1')
select2 = st.sidebar.checkbox('군집2')

selected = []
if select0:
    selected.append(0)
if select1:
    selected.append(1)
if select2:
    selected.append(2)


if selected == []:
    selected = [0]


button0 = st.sidebar.button('침실 수')
button1 = st.sidebar.button('방 수')
button2 = st.sidebar.button('차 수용량')
button3 = st.sidebar.button('전반적인 상태')
button4 = st.sidebar.button('외관 자재 상태')
button5 = st.sidebar.button('지상 거주 면적')
button6 = st.sidebar.button('리모델링 연도')
button7 = st.sidebar.button('진입 도로 유형')
button8 = st.sidebar.button('울타리 유형')
button9 = st.sidebar.button('점수 높은 주택')


col = ['Bedroom_AbvGr', 'TotRms_AbvGrd', 'Garage_Cars', 'Overall_Cond','Exter_Cond', 'g_grlivarea', 'Year_Remod_Add', 'Paved_Drive', 'Fence', 'total']
ft = [globals()[f'button{i}'] for i in np.arange(10)]

if ft == [False,False,False,False,False,False,False,False,False,False]:
    ft = [True,False,False,False,False,False,False,False,False,False]

buttons = [c for c, t in zip(col,ft) if t]

eda_df['Overall_Cond'] = pd.Categorical(eda_df['Overall_Cond'], categories=['Very_Poor','Poor','Fair','Below_Average','Average','Above_Average', 'Good','Very_Good','Excellent'],ordered=True)
eda_df['Exter_Cond'] = pd.Categorical(eda_df['Exter_Cond'], categories=['Fair','Typical','Good','Excellent'],ordered=True)
eda_df['Paved_Drive'] = pd.Categorical(eda_df['Paved_Drive'], categories=['Dirt_Gravel', 'Partial_Pavement', 'Paved'],ordered=True)
eda_df['Fence'] = pd.Categorical(eda_df['Fence'], categories=['No_Fence', 'Minimum_Wood_Wire', 'Good_Wood', 'Minimum_Privacy', 'Good_Privacy'],ordered=True)

if buttons[0] == 'g_grlivarea':
    eda_df['g_grlivarea'] = pd.cut(eda_df['Gr_Liv_Area'], bins=list(range(0,6500,500))).astype('str')
    eda_df['g_grlivarea'] = pd.Categorical(eda_df['g_grlivarea'], categories=['(0, 500]', '(500, 1000]', '(1000, 1500]', '(1500, 2000]', '(2000, 2500]', '(2500, 3000]', '(3000, 3500]', '(3500, 4000]', '(4000, 4500]', '(4500, 5000]', '(5000, 5500]', '(5500, 6000]'])
    g2 = pd.DataFrame(eda_df[eda_df['cluster'].isin(selected)].value_counts(['g_grlivarea','cluster']))
    pivot_df2 = g2.pivot_table(index=buttons[0], columns='cluster', values='count')
    st.bar_chart(pivot_df2, height=400)
elif buttons[0] == 'Year_Remod_Add':
    g3 = eda_df[eda_df['cluster'].isin(selected)].groupby([buttons[0],'cluster'], as_index=False).agg(counts=(buttons[0],'count'))
    pivot_df3 = g3.pivot_table(index=buttons[0],columns='cluster',values='counts')
    st.line_chart(pivot_df3, height=400)
elif buttons[0] == 'total':
    g4 = score_df[(score_df['cluster'].isin(selected)) & (score_df['Paved_Drive']=='Paved')& ((score_df['Fence']=='Good_Privacy') | (score_df['Fence']=='Minimum_Privacy'))].sort_values('total',ascending=False).head(7).reset_index(drop=True)
    pivot_df4 = g4.pivot_table(index='Unnamed: 0', columns='cluster', values='total').sort_values(0,ascending=False)
    pivot_df4.index.name = 'index'
    pivot_df4['max_score'] = pivot_df4.max(axis=1)
    pivot_df4 = pivot_df4.sort_values('max_score', ascending=False).drop(columns='max_score')
    st.bar_chart(pivot_df4, height=400)
else:
    g1 = eda_df[eda_df['cluster'].isin(selected)].groupby([buttons[0],'cluster'], as_index=False).size()
    pivot_df1 = g1.pivot_table(index=buttons[0],columns='cluster',values='size')
    st.bar_chart(pivot_df1, height=400)


st.write('')
st.write('')
st.write('')

# ------------------------------------ plotly
st.subheader('[plotly 시각화] 군집마다 조건별 가구 현황')

st.write('''
plotly 그래프로 알아보기 - 아래 그래프의 왼쪽 버튼을 선택해주세요. 그래프 위에 마우스를 가져다 대면 값을 확인할 수 있습니다.
\n해당 그래프는 각 가구마다 좋은 조건일 수록 높은 점수를 부여한 후, 군집에 묶이지 않은 가구를 제외하고 각 군집마다 가구의 수를 알아본 그래프입니다.
''')
with open('dashboard/img/plotly2.html','r',encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=800, scrolling=False)



