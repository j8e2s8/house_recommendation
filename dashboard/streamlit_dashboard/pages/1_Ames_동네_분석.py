import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ames 동네 분석", page_icon="🗺", layout="wide")

st.title("🗺 Ames 동네 분석")

st.write('---')

# -------------------
st.subheader("Ames 지역 인프라 현황 요약")
st.write('')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📍 Neighborhoods", value="28개")

with col2:
    st.metric(label="💊 Hospital", value="17개")

with col3:
    st.metric(label="🎓 School", value="9개")

st.write('---')

# --------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Ames 동네별 학교와 병원의 위치")
    st.write('''**율이를 위해 학교와 병원의 위치 알기**
    \n점 마크 : 주택 (동네별로 색 구분), 
    \n학교 핀 마크 : 교육기관 (darkgreen색), 
    \n병원 핀 마크 : 의료기관 (orange색)''')
    with open("dashboard/img/Ames_map.html", "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=500, scrolling=False)

with col2:
    st.subheader("DBSCAN 군집화")
    st.write('''**율이를 위해 학교와 병원이 밀집되어 있는 곳 찾기**
    \n학교와 병원이 가까이 모여 있는 지역을 효과적으로 식별하기 위해, min_samples 값을 4가지로 달리하며 최적의 eps를 탐색하여 밀집 지역을 정교하게 군집화했습니다.
    \n※회색 : 밀집되지 않고 군집에서 낙오된 학교와 병원''')
    tab1, tab2, tab3, tab4 = st.tabs(['군집화1','군집화2','군집화3','군집화4'])
    with tab1:
        with open("dashboard/img/DBSCAN_optimal5_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=5, eps=0.000266')
            st.write('군집 1개 - 너무 광범위로 묶임')
            st.components.v1.html(f.read(), height=400, scrolling=False)
    with tab2:
        with open("dashboard/img/DBSCAN_optimal4_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=4, eps=0.000132')
            st.write('군집 3개 - 적절한 거리로 학교와 병원이 골고루 군집됨 [채택]')
            st.components.v1.html(f.read(), height=400, scrolling=False)
    with tab3:
        with open("dashboard/img/DBSCAN_optimal3_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=3, eps=0.000083')
            st.write('군집 2개 - 한 군집이 학교가 없이 병원만 군집됨')
            st.components.v1.html(f.read(), height=400, scrolling=False)
    with tab4:
        with open("dashboard/img/DBSCAN_optimal2_map.html", "r", encoding="utf-8") as f:
            st.write('하이퍼 파라미터 : min_samples=2, eps=0.000031')
            st.write('군집 3개 - 모든 군집이 학교가 없이 병원만 군집됨')
            st.components.v1.html(f.read(), height=400, scrolling=False)

