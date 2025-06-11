# min_samples=4, 최적의 eps=0.000132로 DBSCAN을 한 결과에 대해서
# 해당 군집의 중심 위도, 경도를 찾고, 군집에 포함되는 가구 찾기.
# 관심있는 조건에 대해서 정규화 점수 부여하기
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
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