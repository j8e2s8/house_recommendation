# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| component: valuebox
#| title: Neighborhoods

dict(
  icon = "geo-alt",
  color = "primary",
  value = '28개'
)
#
#
#
#| component: valuebox
#| title: hospital

dict(
  icon = "capsule",
  color = "warning",
  value = '17개'
)
#
#
#
#| component: valuebox
#| title: 'school'

dict(
  icon = "mortarboard",
  color = "info",
  value = '9개'
)
#
#
#
#
#
#
#
#
#
#| title: 'Ames 동네별 학교와 병원 위치'
print("점 마크 : 집 (동네별로 색 구분), 학교 핀 마크 (darkgreen색), 병원 핀 마크 (orange색)")
from IPython.display import IFrame
IFrame('Ames_map.html',width='100%', height='500px')
#
#
#
#
#
#
#
#
#
#
#| title: [DBSCAN 군집화 - min_samples=5, eps=0.000266]
#| padding: 0px

print("군집이 너무 광범위하다")
print("※회색 : 밀집되지 않은 학교와 병원")

from IPython.display import IFrame
IFrame('DBSCAN_optimal5_map.html', width='100%', height='500px')
#
#
#
#
#
#
#| title: [DBSCAN 군집화 - min_samples=4, eps=0.000132]
#| padding: 0px

print("※회색 : 군집되어 있지 않은 학교와 병원")
print("각 군집마다 학교와 병원이 골고루 존재한다. 이 군집에 해당하는 집이 좋을 것 같다.")
from IPython.display import IFrame
IFrame('DBSCAN_optimal4_map.html', width='100%', height='500px')
#
#
#
#
#
#| title: '[DBSCAN 군집화 - min_samples=3, eps=0.000083]'
#| padding: 0px

print("※회색 : 군집되어 있지 않은 학교와 병원")
print("빨간색 군집은 병원밖에 없고, 파란색 군집에 해당하는 집이 좋을 것 같다.")
from IPython.display import IFrame
IFrame('DBSCAN_optimal3_map.html', width='100%', height='500px')
#
#
#
#
#
#| title: '[DBSCAN 군집화 - min_samples=2, eps=0.000031]'
#| padding: 0px

print("※회색 : 군집되어 있지 않은 학교와 병원")
print("너무 최소한의 거리로 군집화를 해서 각 군집에 병원밖에 존재하지 않는다.")
from IPython.display import IFrame
IFrame('DBSCAN_optimal2_map.html', width='100%', height='500px')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| title: '학교와 병원이 밀집되어 있는 세 구역'
#| padding: 0px

from IPython.display import IFrame
IFrame('select_cluster_map.html', width='200%', height='300px')
#
#
#
#
#
#
#
#
#
#
#| title: '조건'
#| padding: 0px

from IPython.display import IFrame
IFrame('../code/plotly.html', width='200%', height='300px')
#
#
#
#
#
