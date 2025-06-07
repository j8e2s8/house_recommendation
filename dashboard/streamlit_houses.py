import streamlit as st
import pandas as pd
import plotly.express as px

# df = pd.read_csv('data/eda_house.csv')

# st.title("🏡 집 추천 시스템")

# with st.sidebar.form(key='my_form'):
#     cluster = st.selectbox("군집 선택", sorted(df['cluster'].unique()))
#     year_range = st.slider("연도 범위", int(df['Year_Remod_Add'].min()), int(df['Year_Remod_Add'].max()), (1980, 2000))
#     submitted = st.form_submit_button("조회")

# if submitted:
#     st.write(f"군집: {cluster}, 연도: {year_range}")


# # cluster = st.sidebar.selectbox("군집 선택", sorted(df['cluster'].unique()))



# filtered_df = df[(df['cluster'] == cluster) & 
#                  (df['Year_Remod_Add'].between(*year_range))]

# group_df = filtered_df.groupby(['Year_Remod_Add'], as_index=False).agg(counts=('Year_Remod_Add','count'))


# # 시각화
# fig = px.line(group_df, 
#               x="Year_Remod_Add", 
#               y="counts", 
#               title=f"군집 {cluster} 리모델링 추이")

# st.plotly_chart(fig)




df = pd.read_csv('data/eda_house.csv')

page = st.sidebar.selectbox("페이지 선택", ["홈", "탐색", "추천"])

if page == "홈":
    st.title("🏠 홈 페이지")
    with st.sidebar.form(key='my_form'):
        cluster = st.selectbox("군집 선택", sorted(df['cluster'].unique()))
        year_range = st.slider("연도 범위", int(df['Year_Remod_Add'].min()), int(df['Year_Remod_Add'].max()), (1980, 2000))
        submitted = st.form_submit_button("조회")

    if submitted:
        st.write(f"군집: {cluster}, 연도: {year_range}")

    filtered_df = df[(df['cluster'] == cluster) & 
                     (df['Year_Remod_Add'].between(*year_range))]

    group_df = filtered_df.groupby(['Year_Remod_Add'], as_index=False).agg(counts=('Year_Remod_Add','count'))


    # 시각화
    fig = px.line(group_df, 
                  x="Year_Remod_Add", 
                  y="counts", 
                  title=f"군집 {cluster} 리모델링 추이")

    st.plotly_chart(fig)

elif page == "탐색":
    st.title("📊 데이터 탐색 페이지")

    cluster2 = st.sidebar.selectbox("군집 선택", sorted(df['cluster'].unique()))
    year_range2 = st.sidebar.slider("연도 범위", int(df['Year_Remod_Add'].min()), int(df['Year_Remod_Add'].max()), (1980, 2000))

    # 필터링
    filtered_df2 = df[(df['cluster'] == cluster2) & 
                    (df['Year_Remod_Add'].between(*year_range2))]
    
    group_df2 = filtered_df2.groupby(['Year_Remod_Add'], as_index=False).agg(counts=('Year_Remod_Add','count'))


    # 시각화
    fig2 = px.line(group_df2, 
                x="Year_Remod_Add", 
                y="counts", 
                title=f"군집 {cluster2} 리모델링 추이")

    st.plotly_chart(fig2)

elif page == "추천":
    st.title("🎯 추천 결과 페이지")
