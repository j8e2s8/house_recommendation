import streamlit as st
import pandas as pd
import numpy as np
import os

# 데이터 불러오기
os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')
score_df = pd.read_csv('./data/score_house.csv')
score_df = score_df.rename(columns={'Unnamed: 0':'house_index'})


# 페이지 설정
st.set_page_config(page_title="선정된 집", page_icon="🏘", layout="wide")

st.title("🏘 조건에 만족하는 집 선정")
st.write('집마다 좋은 조건일 수록 높은 점수를 부여하여 높은 점수를 갖는 집 찾기')

st.write('---')

# ---------------
st.subheader('점수가 높은 순으로 집 확인')
st.write(score_df[score_df['cluster']!=-1].sort_values('total',ascending=False))

# ---------------
st.subheader('점수가 높으면서 포장도로이면서 최소한의 프라이버시를 지켜주는 울타리가 있는 집으로 확인')
st.write(score_df[(score_df['cluster']!=-1)&((score_df['Fence']=='Minimum_Privacy')|(score_df['Fence']=='Good_Privacy'))&(score_df['Paved_Drive']=='Paved')].sort_values('total',ascending=False))


# -----------
st.subheader('선정된 집 확인')
with open('dashboard/selected_house.html','r',encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=800, scrolling=False)


