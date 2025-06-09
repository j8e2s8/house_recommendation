import streamlit as st

# 페이지 설정
st.set_page_config(page_title="결론", page_icon="💡", layout="wide")

st.title("💡 결론")

st.write('---')

st.header('top5 선정된 집의 가격 확인')

st.image("code/houseprice.png", caption="집 가격 분포와 선정된 top5 집의 가격 정도")


col1, col2, col3 = st.columns(3)

with col1:
    st.image("code/oldtown_houseprice.png")

with col2:
    st.image("code/north_ames_houseprice.png")

with col3:
    st.image("code/northwest_ames_houseprice.png")

st.write('2등 집이 조건도 좋고, 가격면에서도 좋아 보입니다.')


st.header('2등 집 위치 확인')
with open('dashboard/final_house.html','r',encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=800, scrolling=False)
