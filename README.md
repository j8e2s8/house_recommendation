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

미국 아이오와주 Ames 시의 주택 거래 데이터 : 79개의 설명 변수와 1개의 목표 변수(SalePrice)로 구성
MSSubClass: 주택 유형을 나타내는 숫자 코드
MSZoning: 일반적인 구역 분류를 나타냅니다.
LotFrontage: 도로와 접한 거리(피트 단위)
LotArea: 대지 면적(평방 피트 단위)
Street: 도로 접근 유형
Alley: 골목 접근 유형
LotShape: 대지 형태
LandContour: 대지의 평탄도
Utilities: 이용 가능한 공공 설비
LotConfig: 대지 구성
LandSlope: 대지의 경사도
Neighborhood: Ames 시 내의 물리적 위치
Condition1: 주요 도로 또는 철도와의 근접성
Condition2: 두 번째 주요 도로 또는 철도와의 근접성
BldgType: 주택 유형
HouseStyle: 주택 스타일
OverallCond: 전반적인 상태 평가
YearBuilt: 원래 건축 연도
YearRemodAdd: 리모델링 또는 증축 연도
RoofStyle: 지붕 스타일
RoofMatl: 지붕 재료
Exterior1st: 외부 마감재(첫 번째)
Exterior2nd: 외부 마감재(두 번째)
MasVnrType: 석조 베니어 유형
MasVnrArea: 석조 베니어 면적(평방 피트 단위)
ExterCond: 외부 재료의 현재 상태
Foundation: 기초 유형
BsmtCond: 지하실 전반적인 상태
BsmtExposure: 지하실 노출 유형
BsmtFinType1: 지하실 마감 유형 1
BsmtFinSF1: 지하실 마감 면적 1(평방 피트 단위)
BsmtFinType2: 지하실 마감 유형 2
BsmtFinSF2: 지하실 마감 면적 2(평방 피트 단위)
BsmtUnfSF: 지하실 미마감 면적(평방 피트 단위)
TotalBsmtSF: 지하실 총 면적(평방 피트 단위)
Heating: 난방 유형
HeatingQC: 난방 품질 및 상태
CentralAir: 중앙 에어컨 유무
Electrical: 전기 시스템
FirstFlrSF: 1층 면적(평방 피트 단위)
SecondFlrSF: 2층 면적(평방 피트 단위)
GrLivArea: 지상 생활 면적(평방 피트 단위)
BsmtFullBath: 지하실 전체 욕실 수
BsmtHalfBath: 지하실 반 욕실 수
FullBath: 전체 욕실 수
HalfBath: 반 욕실 수
BedroomAbvGr: 지상 침실 수
KitchenAbvGr: 지상 주방 수
TotRmsAbvGrd: 지상 총 방 수(욕실 제외)
Functional: 주택 기능성 등급
Fireplaces: 벽난로 수
GarageType: 차고 유형
GarageFinish: 차고 내부 마감 상태
GarageCars: 차고 차량 수용 능력
GarageArea: 차고 면적(평방 피트 단위)
GarageCond: 차고 상태
PavedDrive: 포장된 진입로 유무
WoodDeckSF: 목재 데크 면적(평방 피트 단위)
OpenPorchSF: 오픈 포치 면적(평방 피트 단위)
EnclosedPorch: 밀폐된 포치 면적(평방 피트 단위)
Three_season_porch: 3계절 포치 면적(평방 피트 단위)
ScreenPorch: 스크린 포치 면적(평방 피트 단위)
PoolArea: 수영장 면적(평방 피트 단위)
PoolQC: 수영장 품질
Fence: 울타리 품질
MiscFeature: 기타 특징
MiscVal: 기타 특징의 가치
MoSold: 판매된 월
YearSold: 판매된 연도
SaleType: 판매 유형
SaleCondition: 판매 조건
SalePrice: 판매 가격
Longitude: 경도
Latitude: 위도

---

## 🧠 주요 기술 스택

---

## 📊 결과 요약

---

## 📢 실행 방법