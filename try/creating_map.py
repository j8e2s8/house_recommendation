import folium

# 서울 시청 위치 [위도 37.5665, 경도 126.9780]
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles='OpenStreetMap')
m.save('OpenStreetMap.html')

m = folium.Map(location=[37.5665, 126.9780], zoom_start=3, tiles='cartodbpositron')
m.save('cartodbpositron.html')

m = folium.Map(location=[37.5665, 126.9780], zoom_start=5, tiles='CartoDB positron')
m.save('CartoDB_positron.html')

m = folium.Map(location=[37.5665, 126.9780], zoom_start=10, tiles='CartoDB dark_matter')
m.save('CartoDB_dark_matter.html')

m = folium.Map(location=[37.5665, 126.9780], zoom_start=15, tiles='OpenStreetMap')
m.save('OpenStreetMap_15.html')

m = folium.Map(location=[37.5665, 126.9780], zoom_start=19, tiles='OpenStreetMap')
m.save('OpenStreetMap_19.html')


folium.Marker([37.5665, 126.9780], popup="서울시청").add_to(m)

folium.Marker(
    location,         # [위도, 경도]
    popup=None,       # 마커 클릭 시 뜨는 말풍선 (문자열 또는 HTML)
    tooltip=None,     # 마커에 마우스를 올렸을 때 뜨는 텍스트
    icon=None,        # 마커 모양 설정 (folium.Icon 객체)
    draggable=False   # 마커를 드래그할 수 있는지 여부
)