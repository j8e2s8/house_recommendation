import folium
import base64
import pandas as pd
import numpy as np
import seaborn as sns
import os

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')

# 데이터 불러오기
# house_df = pd.read_csv('../data/raw/houseprice-with-lonlat.csv')
score_df = pd.read_csv('data/score_house.csv')
school_hospital_df = pd.read_csv('data/clustering_school_hospital.csv')

house_df = score_df[(score_df['cluster']!=-1)&((score_df['Fence']=='Minimum_Privacy')|(score_df['Fence']=='Good_Privacy'))&(score_df['Paved_Drive']=='Paved')].sort_values('total',ascending=False).head(20)
house_df = house_df.reset_index()


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



for i, row in house_df.iloc[1:2,:].iterrows():
    encoded = base64.b64encode(open(f'dashboard/streamlit_dashboard/pages/house_top{i+1}.png', 'rb').read()).decode()
    html = f"""
    <h4>순위: {i+1}등 집</h4>
    <img src="data:image/png;base64,{encoded}" width="250"><br>
    <b>동네:</b> {row['Neighborhood']}<br>
    <b>집 가격:</b> ${row['Sale_Price']}<br>
    <b>총점:</b> {np.round(row['total'],2)}점<br>
    <b>침실 수:</b> {row['Bedroom_AbvGr']}개<br>
    <b>방 수:</b> {row['TotRms_AbvGrd']}개<br>
    <b>차 수용량:</b> {row['Garage_Cars']}개<br>
    <b>전반적인 상태:</b> {row['Overall_Cond']}<br>
    <b>외관 상태:</b> {row['Exter_Cond']}<br>
    <b>지상 거주 면적:</b> {row['Lot_Area']} 제곱피트<br>
    <b>리모델링 or 건축 연도:</b> {row['Year_Remod_Add']}<br>
    <b>집입도로 유형:</b> 포장도로<br>
    <b>울타리 유형:</b> {row['Fence']}<br>
    """
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        tooltip=f'{i+1}등 집. 자세한 정보는 클릭하세요.',
        popup = folium.Popup(html, max_width=300) ,
        radius = 30,
        color = 'red',
        opacity = 1,    
        fill = True,
        ).add_to(m)
    


# 지도 저장하기
m.save('dashboard/final_house.html')
