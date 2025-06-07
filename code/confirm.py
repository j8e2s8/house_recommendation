# 데이터 확인하기
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')


# 데이터 불러오기
house_df = pd.read_csv('data/raw/houseprice-with-lonlat.csv')
school_hospital_df = pd.read_csv('data/raw/aims_school_hospital.csv')
score_df = pd.read_csv('data/score_house.csv')
score_df = score_df.sort_values('total',ascending=False)
#school_hospital_df.head(5)

# 지역 수 확인 : 28개
house_df.columns
len(house_df['Neighborhood'].unique())

# 병원 수 확인 : 17개
school_hospital_df[school_hospital_df['type']=='medical'].shape  # (17, 4)

# 학교 수 확인 : 9개
school_hospital_df[school_hospital_df['type']=='school'].shape  # (9, 4)


# 조건이 좋은 집 top5
top_df = score_df[(score_df['cluster']!=-1)&((score_df['Fence']=='Minimum_Privacy')|(score_df['Fence']=='Good_Privacy'))&(score_df['Paved_Drive']=='Paved')].sort_values('total',ascending=False).head(5)
top_df = top_df.reset_index()
# 'Old_Town', 'North_Ames', 'Northwest_Ames'


# 전체 동네 집 가격 분포 그래프
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(6, 4))
plt.title('Ames내에 1~5등 집 가격 정도')
sns.histplot(house_df['Sale_Price'], color='gray')
for i, j in zip(range(5),[4,0,1,3,2]):
    plt.axvline(x=top_df.loc[i,'Sale_Price'], color='red')
    plt.text(top_df.loc[i,'Sale_Price']+5000, 300-30*j, f'{i+1}등 집', color='blue', size=10)
plt.xlabel('Ames 내 집 값')
plt.ylabel('빈도')


# Old_Town동네에 있는 1, 2등 집 가격 정도 그래프
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(6, 4))
plt.title('Old_Town동네에 있는 1, 2등 집 가격 정도')
sns.histplot(house_df[house_df['Neighborhood']=='Old_Town']['Sale_Price'], color='gray')
plt.axvline(x=top_df.loc[0,'Sale_Price'], color='red')
plt.axvline(x=top_df.loc[1,'Sale_Price'], color='red')
plt.text(top_df.loc[0,'Sale_Price']-5000, 40, '1등 집', color='red', size=10, ha='right')
plt.text(top_df.loc[1,'Sale_Price']-5000, 40, '2등 집', color='red', size=10, ha='right')
plt.xlabel('Old_Town동네 집 값')
plt.ylabel('빈도')

# North_Ames동네에 있는 3, 5등 집 가격 정도 그래프
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(6, 4))
plt.title('North_Ames동네에 있는 3, 5등 집 가격 정도')
sns.histplot(house_df[house_df['Neighborhood']=='North_Ames']['Sale_Price'], color='gray')
plt.axvline(x=top_df.loc[2,'Sale_Price'], color='red')
plt.text(top_df.loc[2,'Sale_Price']-5000, 60, '3등 집', color='red', size=10, ha='right')
plt.axvline(x=top_df.loc[4,'Sale_Price'], color='red')
plt.text(top_df.loc[4,'Sale_Price']+5000, 40, '5등 집', color='red', size=10, ha='left')
plt.xlabel('North_Ames동네 집 값')
plt.ylabel('빈도')


# Northwest_Ames동네에 있는 4등 집 가격 정도 그래프
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(6, 4))
plt.title('Northwest_Ames동네에 있는 4등 집 가격 정도')
sns.histplot(house_df[house_df['Neighborhood']=='Northwest_Ames']['Sale_Price'], color='gray')
plt.axvline(x=top_df.loc[3,'Sale_Price'], color='red')
plt.text(top_df.loc[3,'Sale_Price']-5000, 25, '4등 집', color='red', size=10, ha='right')
plt.xlabel('Northwest_Ames동네 집 값')
plt.ylabel('빈도')