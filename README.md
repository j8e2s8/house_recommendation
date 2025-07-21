# 🏠 house_recommendation

사용자의 조건에 따라 학교와 병원이 밀집된 지역을 DBSCAN으로 군집화하고, 각 군집 내에서 고객이 원하는 조건에 맞는 주택을 스코어링하여 Top 5를 지도에 시각화하였습니다.
또한, 지역별 집값이 적정한 수준인지 평가하고, 가장 합리적인 가격의 주택 1건을 최종 추천합니다.
위치 데이터 시각화, 군집 분석, 조건 기반 랭킹, 가격 적정성 평가까지 통합한 실전형 주택 추천 프로젝트입니다.

---

## 📌 프로젝트 개요 및 핵심 기능
- 학교와 병원 위치 기반으로 DBSCAN 최적화를 하여 군집화 진행
- 위치 기반의 집, 학교, 병원의 지도 시각화
- 고객이 원하는 조건에 맞는 주택 스코어링 하여 Top 5 지도 시각화
- 적정 수준의 집 선별하여 주택 1건을 최종 추천

---

## 📝 데이터 소개

### 🔹 데이터 출처
- [Ames Housing Dataset 경로] data/raw/houseprice-with-lonlat.csv
- 아이오와주 Ames 시의 주택 거래 정보와 경도 위도를 담은 공개 데이터셋
- 총 **2,930개 주택**에 대한 **75개 변수** 포함

- [Ames Hospital, School Dataset 경로] data/raw/aims_school_hospital.csv
- 아이오와주 Ames 시의 병원과 학교의 경도 위도를 담은 공개 데이터셋
- 총 **26개 주택**에 대한 **4개 변수** 포함

### 🔹 주요 변수 설명
- houseprice-with-lonlat.csv 

| 변수명           | 설명                    | 예시        |
|-----------------|------------------------|-------------|
| `SalePrice`     | 주택 판매 가격           | 215000      |
| `Bedroom_AbvGr` | 지상 침실 수             | 3           |
| `TotRms_AbvGrd` | 지상 총 방 수            | 7           |
| `Garage_Cars`   | 차량 수용 능력           | 2           |
| `Overall_Cond`  | 주택의 전반적인 상태 평가  | Average     |
| `Exter_Cond`    | 외관 자재의 현재 상태 평가 | Typical     |
| `Gr_Liv_Area`   | 지상 거주 면적 (피트)     | 1656         |
| `Year_Remod_Add`| 리모델링 또는 증축 연도    | 1960        |
| `Paved_Drive`   | 진입로 포장 상태          | Paved       |
| `Fence`         | 울타리 품질              | No_Fence     |
| `Neighborhood`  | Ames 시내의 지역 이름     | North_Ames   |
| `Latitude`      | 주택의 위도              | 42.054035    |
| `Longitude`     | 주택의 경도              | -93.619754   |
 
- aims_school_hospital.csv

| 변수명      | 설명              | 예시                          |
|------------|------------------|-------------------------------|
| `Name`     | 학교 혹은 병원 이름 | Thielen Student Health Cente  |
| `type`     | 학교 or 병원       | medical                      |
| `Latitude` | 건물의 위도        | 42.025756                     |
| `Longitude`| 건물의 경도        | -93.653895                    |

### 🔹 주요 전처리 내용
- 파생 변수 생성: 'Overall_Cond', 'Exter_Cond' 범주 변수를 주거 점수 산정용으로 사용하기 위해 수치화하고, 'Bedroom_AbvGr', 'TotRms_AbvGrd' 등을 포함하여 총 주거 점수 정규화한 변수 생성.


---

## 🧠 주요 기술 스택
- DBSCAN을 이용한 군집화
- folium, plotly, streamlit을 이용한 시각화

---

## 📊 결과 요약
- Old Town에 있는 $184900 가격의 집을 추천함.

---

## 📢 실행 방법
- streamlit : https://houserecommendation-dashboard.streamlit.app/