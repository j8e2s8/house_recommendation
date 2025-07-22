import streamlit as st

# 페이지 설정
st.set_page_config(page_title="결론", page_icon="💡", layout="wide")

st.title("💡 결론")

st.write('---')

st.header('top5 선정된 주택의 가격 확인')

st.image("dashboard/img/houseprice.png", caption="주택 가격 분포와 선정된 top5 주택의 가격 정도")
st.write('')
st.write('')

col1, col2, col3 = st.columns(3)

with col1:
    st.image("dashboard/img/oldtown_houseprice.png")

with col2:
    st.image("dashboard/img/north_ames_houseprice.png")

with col3:
    st.image("dashboard/img/northwest_ames_houseprice.png")

st.write('**2등 주택이 조건도 좋고, 가격면에서도 좋아 보입니다.**')

st.write('---')

st.header('2등 주택 위치 확인')
st.write('점 마크를 클릭하여 2등 주택 정보를 확인하세요.')
with open('dashboard/img/final_house.html','r',encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=800, scrolling=False)
