import streamlit as st

st.set_page_config(page_title="홈", page_icon="🏠", layout="wide")

st.title(":house: 어디로 이사 갈까?")
st.write("(왼쪽 메뉴에서 페이지를 선택하세요.)")


st.write("""
### 팀 : No.1공인중개사
* **조원 :** 윤대웅, 이다경, 장일준, 정은서

### 분석
* **주제 :** Ames에서 조건에 맞는 집 추천
* **데이터**
  * [캐글 : Ames 집 원본 데이터](https://github.com/j8e2s8/Hongdae-Syndrome/blob/main/data/kaggle/houseprice/houseprice-with-lonlat.csv)
  * [Ames 내 학교와 병원 위치 데이터](https://github.com/j8e2s8/Hongdae-Syndrome/blob/main/data/kaggle/houseprice/aims_school_hospital.csv)
""")


col1, col2 = st.columns(2)

with col1:
  st.image('dashboard/img/family.jpg')
  st.image('dashboard/img/house.jpg')

with col2:
  st.write('''여러분 저는 율이를 위해 Ames 지역으로 이사를 준비하고 있습니다.
\n학교와 병원이 가까운 동네 중 조건이 좋은 집으로 추천해주세요.
           
---''')
  st.write('\n')
  st.write('\n')
  st.write('''
\n 중요하게 생각하는 요소 : 
\n \- 집 근처에 학교와 병원이 밀집되어 있는가.
\n \- 집의 주택의 전반적인 상태 평가가 좋은가.
\n \- 집의 외관 자재의 현재 상태 평가가 좋은가.
\n \- 집의 전체 토지 면적이 넓은가.
\n \- 집의 지상 거주 면적이 넓은가.
\n \- 집의 지상 침실 수가 많은가.
\n \- 집의 지상 층의 총 방 개수 (욕실 제외)가 많은가.
\n \- 집의 차량 수용 능력이 많은가.
\n \- 집의 진입로 포장 상태가 전면 포장인가.
\n \- 집의 울타리가 적어도 최소한의 프라이버시 울타리인가.
\n \- 집의 건축 연도 혹은 리모델링 연도가 최근인가. ''')