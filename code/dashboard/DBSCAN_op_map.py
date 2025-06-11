# min_samples별 최적의 eps로, 병원과 학교 그룹화에 대한 지도 그리기
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import folium
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

# 데이터 불러오기

house_df = pd.read_csv('../data/raw/houseprice-with-lonlat.csv')
school_hospital_df = pd.read_csv('../data/clustering_school_hospital.csv', index=False)




# ------------------------- 최적의 min_samples, eps로 지도 그리기

# 색 딕셔너리 만들기
neighborhoods = house_df['Neighborhood'].unique()
palette = sns.color_palette("hls", len(neighborhoods))  # hls는 고르게 퍼진 색을 의미

color_dict = {
    nb: f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
    for nb, (r, g, b) in zip(neighborhoods, palette)
}

# 지도 만들기
m = folium.Map(location=[42.030806089293755, -93.6304970070205], zoom_start=13, tiles='CartoDB positron')


# 라디안 변환
min_samples = [2,3,4,5]

for i in min_samples:

    # --------------------------- 지도 그리기
    # 지도에 마크 표시
    for _, row in school_hospital_df.iterrows():
        if (row[f'cluster_minsample{i}_op']==-1)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip= row['Name'],
                icon= folium.Icon(color='lightgray',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==-1)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip= row['Name'],
                icon= folium.Icon(color='lightgray',icon='graduation-cap', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==0)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='darkred',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==0)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='darkred',icon='graduation-cap', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==1)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='darkblue',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==1)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='darkblue',icon='graduation-cap', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==2)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='purple',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==2)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='purple',icon='graduation-cap', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==3)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='darkgreen',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==3)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='darkgreen',icon='graduation-cap', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==4)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='green',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==4)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='green',icon='graduation-cap', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==5)&(row['type']=='medical'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='cadetblue',icon='user-md', prefix='fa')
                ).add_to(m)
        elif (row[f'cluster_minsample{i}_op']==5)&(row['type']=='school'):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                tooltip=row['Name'],
                icon= folium.Icon(color='cadetblue',icon='graduation-cap', prefix='fa')
                ).add_to(m)
            

    for _, row in house_df.iterrows():
        select_color = color_dict.get(row['Neighborhood'], 'grey')
        folium.Circle(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f'{row['Unnamed: 0']}번째 집',
            radius = 20,
            color = select_color,
            opacity = 0.5,    
            fill = True,
            ).add_to(m)

    # 지도 저장하기
    # m.save(f'DBSCAN_optimal{i}_map.html')

