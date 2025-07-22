import streamlit as st
import pandas as pd
import numpy as np
import os

# 데이터 불러오기
score_df = pd.read_csv('data/score_house.csv')
score_df = score_df.rename(columns={'Unnamed: 0':'house_index'})


# 페이지 설정
st.set_page_config(page_title="선정된 주택", page_icon="🏘", layout="wide")

st.title("🏘 조건에 만족하는 주택 선정")
st.write('주택마다 좋은 조건일 수록 높은 점수를 부여하여 높은 점수를 갖는 주택 찾기')

st.write('---')
st.write('')
st.write('')

# ---------------
st.subheader('점수기반 주택 순위')
st.write(score_df[score_df['cluster']!=-1].sort_values('total',ascending=False).reset_index())
st.write('')
st.write('')
st.write('')
st.write('')

# ---------------
st.subheader('점수기반 조건에 충족하는 주택 순위')
st.write('고객이 원하는 조건 : 포장도로, 최소한의 프라이버시를 지켜주는 울타리')
st.write(score_df[(score_df['cluster']!=-1)&((score_df['Fence']=='Minimum_Privacy')|(score_df['Fence']=='Good_Privacy'))&(score_df['Paved_Drive']=='Paved')].sort_values('total',ascending=False).reset_index())
st.write('')
st.write('')
st.write('')
st.write('')

# -----------
st.subheader('선정된 주택 확인')
st.write('점 마크를 클릭하여 top5 주택 정보를 확인하세요.')
with open('dashboard/img/selected_house.html','r',encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=500, scrolling=False)


