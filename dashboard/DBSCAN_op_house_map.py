# min_samples=4, 최적의 eps=0.000132로 DBSCAN을 한 군집과 그 군집에 해당하는 가구 지도 그리기
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import folium
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
eda_df = pd.read_csv('../data/eda_house.csv')
school_hospital_loc = pd.read_csv('../data/clustering_school_hospital.csv')



# --------------------------- 지도 그리기
# 지도 만들기
m = folium.Map(location=[42.022626, -93.604193], zoom_start=12, tiles='CartoDB positron')



# 지도에 마크 표시
for _, row in school_hospital_loc.iterrows():
    if (row[f'cluster_minsample4_op']==-1)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip= row['Name'],
            icon= folium.Icon(color='lightgray',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==-1)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip= row['Name'],
            icon= folium.Icon(color='lightgray',icon='graduation-cap', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==0)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkred',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==0)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkred',icon='graduation-cap', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==1)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkblue',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==1)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkblue',icon='graduation-cap', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==2)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='purple',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==2)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='purple',icon='graduation-cap', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==3)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkgreen',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==3)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkgreen',icon='graduation-cap', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==4)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='green',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==4)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='green',icon='graduation-cap', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==5)&(row['type']=='medical'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='cadetblue',icon='user-md', prefix='fa')
            ).add_to(m)
    elif (row[f'cluster_minsample4_op']==5)&(row['type']=='school'):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='cadetblue',icon='graduation-cap', prefix='fa')
            ).add_to(m)
            

for _, row in eda_df.iterrows():
    if (row[f'distance_from_cluster0']<=0.000132):
        folium.Circle(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f'{row['Unnamed: 0']}번째 집, {row['Sale_Price']} 달러, {row['Neighborhood']} 동네',
            radius = 20,
            color = 'darkred',
            opacity = 0.5,    
            fill = True,    
            ).add_to(m)
    elif (row[f'distance_from_cluster1']<=0.000132):
        folium.Circle(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f'{row['Unnamed: 0']}번째 집, {row['Sale_Price']} 달러, {row['Neighborhood']} 동네',
            radius = 20,
            color = 'darkblue',
            opacity = 0.5,    
            fill = True,    
            ).add_to(m)
    elif (row[f'distance_from_cluster2']<=0.000132):
        folium.Circle(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f'{row['Unnamed: 0']}번째 집, {row['Sale_Price']} 달러, {row['Neighborhood']} 동네',
            radius = 20,
            color = 'purple',
            opacity = 0.5,    
            fill = True,    
            ).add_to(m)
    else:
        folium.Circle(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f'{row['Unnamed: 0']}번째 집, {row['Sale_Price']} 달러, {row['Neighborhood']} 동네',
            radius = 20,
            color = 'lightgray',
            opacity = 0.5,    
            fill = True,    
            ).add_to(m)

# 지도 저장하기
m.save(f'select_cluster_map.html')

