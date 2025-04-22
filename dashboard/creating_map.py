import folium
import pandas as pd

school_hospital_df = pd.read_csv('../data/aims_school_hospital.csv')

school_hospital_df['type'].unique()  # 'medical', 'school'


# 지도 만들기기
m = folium.Map(location=[42.030806089293755, -93.6304970070205], zoom_start=13, tiles='CartoDB positron')

# 지도에 마크 표시시
for _, row in school_hospital_df.iterrows():
    if row['type']=='medical':
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='orange',icon='user-md', prefix='fa')
            ).add_to(m)
    elif row['type']=='school':
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon= folium.Icon(color='darkgreen',icon='graduation-cap', prefix='fa')
            ).add_to(m)

m.save('Ames_map.html')