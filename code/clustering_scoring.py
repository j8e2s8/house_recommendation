# min_samples=4, 최적의 eps=0.000132로 DBSCAN을 한 결과에 대해서
# 해당 군집의 중심 위도, 경도를 찾고, 군집에 포함되는 가구 찾기.
# 관심있는 조건에 대해서 정규화 점수 부여하기
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import os

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')


# 데이터 불러오기
house_df = pd.read_csv('data/raw/houseprice-with-lonlat.csv')
school_hospital_loc = pd.read_csv('data/clustering_school_hospital.csv')


school_hospital_loc.columns

# 그룹 방식별 각 그룹마다 평균 위도, 경도
school_hospital_loc.groupby('cluster')[['Latitude','Longitude']].mean()
school_hospital_loc.groupby('cluster_minsample2_op')[['Latitude','Longitude']].mean() # 최적의 eps = 0.000031
school_hospital_loc.groupby('cluster_minsample3_op')[['Latitude','Longitude']].mean() # 최적의 eps = 0.000083
school_hospital_loc.groupby('cluster_minsample4_op')[['Latitude','Longitude']].mean() # 최적의 eps = 0.000132
school_hospital_loc.groupby('cluster_minsample5_op')[['Latitude','Longitude']].mean() # 최적의 eps = 0.000266

# 우리가 사용할 그룹 방식 : 'cluster_minsample4_op'
cluster_dict = school_hospital_loc.groupby('cluster_minsample4_op')[['Latitude','Longitude']].mean().T.to_dict()



# 거리 계산 함수
def haversine_radian_distance(lat1, lon1, lat2, lon2):
    # 위도/경도를 라디안으로 변환
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # 거리 계산
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    radian_distance = 2 * np.arcsin(np.sqrt(a))  
    
    return radian_distance


# 각 군집 중심과 가구와의 거리를 구해서, eps=0.000132 거리에 포함되는 가구 찾기.
# 가구마다 해당하는 cluster 컬럼 지정.
house_df['cluster'] = np.nan
for i in cluster_dict.keys():
    if i != -1:
        center_lat = cluster_dict[i]['Latitude']
        center_lon = cluster_dict[i]['Longitude']
        house_df[f'distance_from_cluster{i}'] = house_df.apply(
            lambda row: haversine_radian_distance(center_lat, center_lon, row['Latitude'], row['Longitude']), axis=1
        )
        house_df.loc[house_df[f'distance_from_cluster{i}'] <= 0.000132 , 'cluster'] = i
    elif i == -1:
        house_df['cluster'].fillna(-1, inplace=True)

house_df.columns

house_df['cluster'] = house_df['cluster'].astype(int)
house_df['cluster'].unique()


# 데이터 저장하기
# house_df.to_csv('../data/eda_house.csv' , index=False )




# 관심 있는 조건 : 
# Lot_Area, Bedroom_AbvGr, TotRms_AbvGrd, Gr_Liv_Area, Garage_Cars 수치가 큰 곳
# Overall_Cond, Exter_Cond 범주가 높은 곳
# Condition_1, Condition_2 가 PosN, PosA 인 곳
# Paved_Drive Paved 인 곳
# Fence Good_Privacy, Minimum_Privacy인 곳
# Year_Remod_Add 최근 인 곳

house_df.columns

house_df['Lot_Area'].describe
house_df['Bedroom_AbvGr'].unique()
house_df['TotRms_AbvGrd'].unique()
house_df['Gr_Liv_Area'].describe
house_df['Garage_Cars'].unique()

house_df['Overall_Cond'].unique()
house_df['Exter_Cond'].unique()

house_df['Condition_1'].unique()
house_df['Paved_Drive'].unique()
house_df['Fence'].unique()

house_df['Year_Remod_Add'].unique()




# 범주 컬럼에에 점수 부여하기
Overall_Cond_map = {
	'Very_Poor':0.0,
    'Poor':0.1,
    'Fair':0.2,
    'Below_Average':0.3,
    'Average':0.4,
    'Above_Average':0.5,
    'Good':0.6,
    'Very_Good':0.8,
    'Excellent':1.0
}
house_df['OverallCond_score'] = house_df['Overall_Cond'].map(Overall_Cond_map)
house_df['OverallCond_score'].unique()


Exter_Cond_map = {
	'Excellent': 1.0,
	'Good': 0.8,
	'Typical': 0.6,
	'Fair': 0.4,
	'Poor': 0.0
}
house_df['ExterCond_score'] = house_df['Exter_Cond'].map(Exter_Cond_map)
house_df['ExterCond_score'].unique()


# 관심있는 컬럼 정규화해서 total 점수 컬럼 만들기
scaler = MinMaxScaler()
scaler_np = scaler.fit_transform(house_df[['Lot_Area', 'Bedroom_AbvGr', 'TotRms_AbvGrd','Gr_Liv_Area','Garage_Cars', 'Year_Remod_Add']])
scaler_df = pd.DataFrame(scaler_np, columns=['norm_Lot_Area', 'norm_Bedroom_AbvGr', 'norm_TotRms_AbvGrd','norm_Gr_Liv_Area','norm_Garage_Cars', 'norm_Year_Remod_Add'], index=house_df.index)
score_df = pd.concat([house_df[['Unnamed: 0','Neighborhood','ExterCond_score','Exter_Cond', 'OverallCond_score','Overall_Cond', 'Condition_1', 'Condition_2', 'Paved_Drive', 'Fence','cluster','Sale_Price','Longitude','Latitude','Lot_Area','Bedroom_AbvGr','TotRms_AbvGrd','Gr_Liv_Area','Garage_Cars','Year_Remod_Add']],scaler_df], axis=1)
score_df['total'] = score_df[['ExterCond_score', 'OverallCond_score','norm_Lot_Area', 'norm_Bedroom_AbvGr', 'norm_TotRms_AbvGrd','norm_Gr_Liv_Area','norm_Garage_Cars', 'norm_Year_Remod_Add']].apply(sum, axis=1) # 최대 8점

score_df.sort_values('total', ascending=False)



# 데이터 저장하기
# score_df.to_csv('data/score_house.csv' , index=False )






