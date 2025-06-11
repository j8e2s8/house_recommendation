import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ames 동네 분석", page_icon="🗺", layout="wide")

st.title("🗺 Ames 동네 분석")

st.write('---')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📍 Neighborhoods", value="28개")

with col2:
    st.metric(label="💊 Hospital", value="17개")

with col3:
    st.metric(label="🎓 School", value="9개")


st.write('---')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ames 동네별 학교와 병원의 위치")
    st.write('''**율이를 위해 학교와 병원의 위치 알기**
    \n점 마크 : 집 (동네별로 색 구분), 
    \n학교 핀 마크 (darkgreen색), 
    \n병원 핀 마크 (orange색)''')
    with open("dashboard/img/Ames_map.html", "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=500, scrolling=False)

with col2:
    st.subheader("DBSCAN 군집화")
    st.write('''**율이를 위해 학교와 병원이 밀집되어 있는 곳 찾기**
    \n※회색 : 밀집되지 않고 군집에서 낙오된 학교와 병원''')
    tab1, tab2, tab3, tab4 = st.tabs(['군집화1','군집화2','군집화3','군집화4'])
    with tab1:
        with open("dashboard/img/DBSCAN_optimal5_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=5, eps=0.000266')
            st.components.v1.html(f.read(), height=400, scrolling=False)
    with tab2:
        with open("dashboard/img/DBSCAN_optimal4_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=4, eps=0.000132')
            st.components.v1.html(f.read(), height=400, scrolling=False)
    with tab3:
        with open("dashboard/img/DBSCAN_optimal3_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=3, eps=0.000083')
            st.components.v1.html(f.read(), height=400, scrolling=False)
    with tab4:
        with open("dashboard/img/DBSCAN_optimal2_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=2, eps=0.000031')
            st.components.v1.html(f.read(), height=400, scrolling=False)

