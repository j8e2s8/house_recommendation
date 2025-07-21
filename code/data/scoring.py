import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import os


# 데이터 불러오기
house_df = pd.read_csv('../data/eda_house.csv')

# 관심 있는 조건 : 
# Bedroom_AbvGr, TotRms_AbvGrd, Gr_Liv_Area, Garage_Cars 수치가 큰 곳
# Overall_Cond, Exter_Cond 범주가 높은 곳
# Paved_Drive Paved 인 곳
# Fence Good_Privacy, Minimum_Privacy인 곳
# Year_Remod_Add 최근 인 곳

house_df.columns

house_df['Bedroom_AbvGr'].unique()
house_df['TotRms_AbvGrd'].unique()
house_df['Gr_Liv_Area'].describe
house_df['Garage_Cars'].unique()

house_df['Overall_Cond'].unique()
house_df['Exter_Cond'].unique()

house_df['Paved_Drive'].unique()
house_df['Fence'].unique()

house_df['Year_Remod_Add'].unique()




# 범주 컬럼에에 점수 부여하기
Overall_Cond_map = {
	'Very_Poor':0.0,
    'Poor':0.1,
    'Fair':0.2,
    'Below_Average':0.3,
    'Average':0.4,
    'Above_Average':0.5,
    'Good':0.6,
    'Very_Good':0.8,
    'Excellent':1.0
}
house_df['OverallCond_score'] = house_df['Overall_Cond'].map(Overall_Cond_map)
house_df['OverallCond_score'].unique()


Exter_Cond_map = {
	'Excellent': 1.0,
	'Good': 0.8,
	'Typical': 0.6,
	'Fair': 0.4,
	'Poor': 0.0
}
house_df['ExterCond_score'] = house_df['Exter_Cond'].map(Exter_Cond_map)
house_df['ExterCond_score'].unique()


# 관심있는 컬럼 정규화해서 total 점수 컬럼 만들기
scaler = MinMaxScaler()
scaler_np = scaler.fit_transform(house_df[['Bedroom_AbvGr', 'TotRms_AbvGrd','Gr_Liv_Area','Garage_Cars', 'Year_Remod_Add']])
scaler_df = pd.DataFrame(scaler_np, columns=['norm_Bedroom_AbvGr', 'norm_TotRms_AbvGrd','norm_Gr_Liv_Area','norm_Garage_Cars', 'norm_Year_Remod_Add'], index=house_df.index)
score_df = pd.concat([house_df[['Unnamed: 0','Neighborhood','ExterCond_score','Exter_Cond', 'OverallCond_score','Overall_Cond', 'Paved_Drive', 'Fence','cluster','Sale_Price','Longitude','Latitude','Bedroom_AbvGr','TotRms_AbvGrd','Gr_Liv_Area','Garage_Cars','Year_Remod_Add']],scaler_df], axis=1)
score_df['total'] = score_df[['ExterCond_score', 'OverallCond_score', 'norm_Bedroom_AbvGr', 'norm_TotRms_AbvGrd','norm_Gr_Liv_Area','norm_Garage_Cars', 'norm_Year_Remod_Add']].apply(sum, axis=1) # 최대 8점

score_df.sort_values('total', ascending=False)



# 데이터 저장하기
# score_df.to_csv('data/score_house.csv' , index=False )






