import folium
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# 데이터 불러오기
house_df = pd.read_csv('../data/houseprice-with-lonlat.csv')
school_hospital_df = pd.read_csv('../data/aims_school_hospital.csv')

school_hospital_df['type'].unique()  # 'medical', 'school'
house_df.head(5)
house_df.columns
len(house_df['Neighborhood'].unique())


# 색 딕셔너리 만들기
neighborhoods = house_df['Neighborhood'].unique()
palette = sns.color_palette("hls", len(neighborhoods))  # hls는 고르게 퍼진 색을 의미

color_dict = {
    nb: f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
    for nb, (r, g, b) in zip(neighborhoods, palette)
}


# 지도 만들기
m = folium.Map(location=[42.030806089293755, -93.6304970070205], zoom_start=13, tiles='CartoDB positron')

# 지도에 마크 표시
for _, row in school_hospital_df.iterrows():
    if row['type']=='medical':
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip= row['Name'],
            icon= folium.Icon(color='orange',icon='user-md', prefix='fa')
            ).add_to(m)
    elif row['type']=='school':
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkgreen',icon='graduation-cap', prefix='fa')
            ).add_to(m)
        

for _, row in house_df.iterrows():
    select_color = color_dict.get(row['Neighborhood'], 'grey')
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        tooltip=f'{row['Unnamed: 0']}번째 집',
        radius = 3,
        color = select_color,
        opacity = 0.5,    
        fill = True,
        ).add_to(m)

# 지도 저장하기
m.save('Ames_map.html')
