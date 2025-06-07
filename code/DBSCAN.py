# min_samples별 최적의 eps로, 병원과 학교 그룹화
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
school_hospital_df = pd.read_csv('../data/raw/aims_school_hospital')


# -------------------------- DBSCAN의 각 min_samples 마다 최적의 eps 구하기
# 데이터간 거리를 봤을 때 상대적으로 갑자기 멀어지는 거리를 기준으로 적절한 eps 거리 구하기
def optimized_dbscan(df, min_samples, metric='euclidean'):
    from sklearn.neighbors import NearestNeighbors
    if metric=='haversine':
        coords = np.radians(df[['Latitude', 'Longitude']].values)

    nn = NearestNeighbors(n_neighbors=min_samples, metric=metric)
    nn.fit(coords)  

    distances, indices = nn.kneighbors(coords)

    df2 = df.copy()

    # 이웃 거리를 포함한 데이터셋 만들기
    for i in np.arange(min_samples):
        if i >=1:
            df2[f"nn{i}_distance"] = distances[:,i]
            df2[f"nn{i}_index"] = indices[:,i]

    # 그래프를 위한 각 데이터마다 제일 멀리 있는 마지막 이웃의 거리만 뽑기
    k_distances = distances[:, min_samples-1]  


    # 급격히 변하는 거리 값 구하기
    from kneed import KneeLocator

    kneedle = KneeLocator(range(len(k_distances)), k_distances, curve="convex", direction="increasing")
    eps_optimal = k_distances[kneedle.knee]
    print(f"최적의 eps (방법: {metric}): {eps_optimal: .10f}")
    
    # 그래프
    plt.figure(figsize=(10, 5))
    plt.plot(np.sort(k_distances)) # 오름차순으로 거리 그래프 그리기
    plt.axhline(y=eps_optimal, color ='red')
    plt.ylabel(f"{min_samples}-th Nearest Neighbor Distance (방법 : {metric})")
    plt.xlabel("Points sorted by distance")
    plt.title(f"DBSCAN eps 거리 값 선택을 위한 {min_samples}nn-distance 그래프")
    plt.text(len(k_distances)*0.8, eps_optimal, '급격히 변한 거리값', ha='center', va = 'bottom',color = 'red')
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.grid(True)
    plt.show()

    return {'df':df2, 'eps_optimal' : eps_optimal}


# optimized_dbscan(school_hospital_df, 3, metric='haversine')['eps_optimal']



# 각 min_samples 마다 최적의 eps 구하기
op_eps_df = pd.DataFrame({})
min_samples = [2,3,4,5]
op_eps = []

for i in min_samples:
    print(f"min_samples = {i} 에 대해서")
    op_eps.append(optimized_dbscan(school_hospital_df, i, metric='haversine')['eps_optimal'])
    
op_eps_df = pd.DataFrame({'min_samples' :min_samples , 'op_eps' : op_eps })


display(op_eps_df)

# min_samples	op_eps
#  	2	0.000031
#  	3	0.000083
#  	4	0.000132
#  	5	0.000266



# 각 min_samples 마다 최적의 eps로 가구들 그룹화하기 [4가지 방법]
coords = np.radians(school_hospital_df[['Latitude', 'Longitude']].values)

for index, i in enumerate(min_samples):
    print(f"min_samples={i}에 대해서")
    db = DBSCAN(eps=op_eps_df.iloc[index,1], min_samples=i, metric='haversine').fit(coords)
    school_hospital_df[f'cluster_minsample{i}_op'] = db.labels_


# 데이터 저장하기
# school_hospital_df.to_csv('../data/clustering_school_hospital.csv', index=False)

