import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')



eda_df = pd.read_csv('./data/eda_house.csv')
score_df = pd.read_csv('./data/score_house.csv')

g1 = eda_df[eda_df['cluster']!= -1].groupby(['Bedroom_AbvGr','cluster'], as_index=False).agg(counts=('Bedroom_AbvGr','count'))
g2 = eda_df[eda_df['cluster']!= -1].groupby(['TotRms_AbvGrd','cluster'], as_index=False).agg(counts=('TotRms_AbvGrd','count'))
g3 = eda_df[eda_df['cluster']!= -1].groupby(['Garage_Cars','cluster'], as_index=False).agg(counts=('Garage_Cars','count'))
g4 = eda_df[eda_df['cluster']!= -1].groupby(['Overall_Cond','cluster'], as_index=False).agg(counts=('Overall_Cond','count'))
g5 = eda_df[eda_df['cluster']!= -1].groupby(['Exter_Cond','cluster'], as_index=False).agg(counts=('Exter_Cond','count'))
eda_df['g_grlivarea'] = pd.cut(eda_df['Gr_Liv_Area'], bins=list(range(0,6500,500)))
g9 = pd.DataFrame(eda_df[eda_df['cluster']!= -1].value_counts(['g_grlivarea','cluster']))
g8 = eda_df[eda_df['cluster']!= -1].groupby(['Year_Remod_Add','cluster'], as_index=False).agg(counts=('Year_Remod_Add','count'))
pivot_df8 = g8.pivot_table(index='Year_Remod_Add',columns='cluster',values='counts')
g6 = eda_df[eda_df['cluster']!= -1].groupby(['Paved_Drive','cluster'], as_index=False).agg(counts=('Paved_Drive','count'))
g7 = eda_df[eda_df['cluster']!= -1].groupby(['Fence','cluster'], as_index=False).agg(counts=('Fence','count'))
g10 = score_df[(score_df['cluster']!= -1) & (score_df['Paved_Drive']=='Paved')& ((score_df['Fence']=='Good_Privacy') | (score_df['Fence']=='Minimum_Privacy'))].sort_values('total',ascending=False).head(7).reset_index(drop=True)
pivot_df10 = g10.pivot_table(index='Unnamed: 0',columns='cluster', values='total')


fig = go.Figure()

# 두 개의 그래프 trace
fig.add_trace(go.Bar(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.add_trace(go.Bar(x=g2[g2['cluster']==0]['TotRms_AbvGrd'].astype('str') , y=g2[g2['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g2[g2['cluster']==2]['TotRms_AbvGrd'].astype('str') , y=g2[g2['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g2[g2['cluster']==1]['TotRms_AbvGrd'].astype('str') , y=g2[g2['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.add_trace(go.Bar(x=g3[g3['cluster']==0]['Garage_Cars'].astype('str') , y=g3[g3['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g3[g3['cluster']==2]['Garage_Cars'].astype('str') , y=g3[g3['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g3[g3['cluster']==1]['Garage_Cars'].astype('str') , y=g3[g3['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.add_trace(go.Bar(x=g4[g4['cluster']==0]['Overall_Cond'].astype('str') , y=g4[g4['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g4[g4['cluster']==2]['Overall_Cond'].astype('str') , y=g4[g4['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g4[g4['cluster']==1]['Overall_Cond'].astype('str') , y=g4[g4['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.add_trace(go.Bar(x=g5[g5['cluster']==0]['Exter_Cond'].astype('str') , y=g5[g5['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g5[g5['cluster']==2]['Exter_Cond'].astype('str') , y=g5[g5['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g5[g5['cluster']==1]['Exter_Cond'].astype('str') , y=g5[g5['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.add_trace(go.Bar(x=g9.xs(0, level='cluster').index.get_level_values('g_grlivarea').astype('str') , y=g9.xs(0, level='cluster').values.reshape(1,-1)[0]
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g9.xs(2, level='cluster').index.get_level_values('g_grlivarea').astype('str') , y=g9.xs(2, level='cluster').values.reshape(1,-1)[0]
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g9.xs(1, level='cluster').index.get_level_values('g_grlivarea').astype('str') , y=g9.xs(1, level='cluster').values.reshape(1,-1)[0]
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.add_trace(go.Scatter(x=pivot_df8.index , y=pivot_df8[0]
                , mode='lines+markers' ,marker=dict(size=3, color='darkred'), line=dict(width=1),name="군집0", showlegend=True))
fig.add_trace(go.Scatter(x=pivot_df8.index , y=pivot_df8[2]
                    , mode='lines+markers' ,marker=dict(size=3, color='purple'), line=dict(width=1),name="군집1", showlegend=True))
fig.add_trace(go.Scatter(x=pivot_df8.index , y=pivot_df8[1]
                    , mode='lines+markers' ,marker=dict(size=3, color='darkblue'), line=dict(width=1),name="군집2", showlegend=True))

fig.add_trace(go.Bar(x=g6[g6['cluster']==0]['Paved_Drive'].astype('str') , y=g6[g6['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g6[g6['cluster']==2]['Paved_Drive'].astype('str') , y=g6[g6['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g6[g6['cluster']==1]['Paved_Drive'].astype('str') , y=g6[g6['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.add_trace(go.Bar(x=g7[g7['cluster']==0]['Fence'].astype('str') , y=g7[g7['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g7[g7['cluster']==2]['Fence'].astype('str') , y=g7[g7['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g7[g7['cluster']==1]['Fence'].astype('str') , y=g7[g7['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.add_trace(go.Bar(x=pivot_df10.index.astype('str') , y=pivot_df10[0]
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=pivot_df10.index.astype('str') , y=pivot_df10[2]
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))



bed_shape = []
bed_bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
for b in bed_bins:
    bed_shape.append(dict(type='line',x0=b,x1=b,y0=g1['counts'].min()-1, y1=g1['counts'].max()+10,line=dict(color='gray',width=2,dash='dash')))

bed_annotation = []
bed_bins2 = [0,1,2,3,4,5,6]
bed_text = np.sort(score_df['norm_Bedroom_AbvGr'].unique().round(2))[:-1]
for b, t in zip(bed_bins2, bed_text):
    bed_annotation.append(dict(x=b,y=170,text=f'{t}점수 부여', showarrow=False, font=dict(size=9, color='gray')))

room_shape = []
room_bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]
for b in room_bins:
    room_shape.append(dict(type='line',x0=b,x1=b,y0=g2['counts'].min()-1, y1=g2['counts'].max()+20,line=dict(color='gray',width=2,dash='dash')))

room_annotation = []
room_bins2 = [0,1,2,3,4,5,6,7,8,9]
room_text = np.sort(score_df['norm_TotRms_AbvGrd'].unique().round(2))[1:-3]
for b, t in zip(room_bins2, room_text):
    room_annotation.append(dict(x=b,y=130,text=f'{t}점수 부여', showarrow=False, font=dict(size=9, color='gray')))

car_shape = []
car_bins = [0.5, 1.5, 2.5, 3.5]
for b in car_bins:
    car_shape.append(dict(type='line',x0=b,x1=b,y0=g3['counts'].min()-1, y1=g3['counts'].max()+20,line=dict(color='gray',width=2,dash='dash')))

car_annotation = []
car_bins2 = [0,1,2,3,4]
car_text = np.sort(score_df['norm_Garage_Cars'].unique().round(2))[:-1]
for b, t in zip(car_bins2, car_text):
    car_annotation.append(dict(x=b,y=200,text=f'{t}점수 부여', showarrow=False, font=dict(size=9, color='gray')))

con_shape = []
con_bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
for b in con_bins:
    con_shape.append(dict(type='line',x0=b,x1=b,y0=g4['counts'].min()-1, y1=g4['counts'].max()+20,line=dict(color='gray',width=2,dash='dash')))

con_annotation = []
con_bins2 = [0,1,2,3,4,5,6,7,8]
con_text = np.sort(score_df[score_df['cluster']!=-1]['OverallCond_score'].unique().round(2))
for b, t in zip(con_bins2, con_text):
    con_annotation.append(dict(x=b,y=105,text=f'{t}점수 부여', showarrow=False, font=dict(size=9, color='gray')))

out_shape = []
out_bins = [0.5, 1.5, 2.5]
for b in out_bins:
    out_shape.append(dict(type='line',x0=b,x1=b,y0=g5['counts'].min()-1, y1=g5['counts'].max()+20,line=dict(color='gray',width=2,dash='dash')))

out_annotation = []
out_bins2 = [0,1,2,3]
out_text = np.sort(score_df[score_df['cluster']!=-1]['ExterCond_score'].unique().round(2))
for b, t in zip(out_bins2, out_text):
    out_annotation.append(dict(x=b,y=310,text=f'{t}점수 부여', showarrow=False, font=dict(size=9, color='gray')))


fig.update_layout(
    autosize=True,
    updatemenus=[
        dict(type='buttons',
             x=-0.1,
             buttons=[
                dict( label='침실 수', method ='update', 
                      args=[{'visible':[True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 침실 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title=dict(text='침실 수 (침실이 많을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['0','1','2','3','4','5','6'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : bed_shape
                              , 'annotations' : bed_annotation}
                            ]
                        ),
                dict( label='방 수', method ='update', 
                      args=[{'visible':[False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 방 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              ,'xaxis' : dict(title=dict(text='방 수 (방이 많을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['3','4','5','6','7','8','9','10','11','12'])
                              , 'shapes' : room_shape
                              , 'annotations' : room_annotation}
                            ]
                        ),
                dict( label='차 수용량', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 차 수용량별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='차 수용량 (차 수용량이 많을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['0','1','2','3','4'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : car_shape
                              , 'annotations' : car_annotation}
                            ]
                        ),
                dict( label='전반적인 상태', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 전반적인 상태별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='전반적인 상태 (전반적인 상태가 좋을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['Very_Poor','Poor','Fair','Below_Average','Average','Above_Average', 'Good','Very_Good','Excellent'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : con_shape
                              , 'annotations' : con_annotation}
                            ]
                        ),
                dict( label='외관 자재 상태', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 외관 자재 상태별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='외관 자재 상태 (외관 자재 상태가 좋을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['Fair','Typical','Good','Excellent'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : out_shape
                              , 'annotations' : out_annotation}
                            ]
                        ),
                 dict( label='지상 거주 면적', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 지상 거주 면적별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='지상 거주 면적 구간 (지상 거주 면적이 넓을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['(0, 500]', '(500, 1000]', '(1000, 1500]', '(1500, 2000]', '(2000, 2500]', '(2500, 3000]', '(3000, 3500]', '(3500, 4000]', '(4000, 4500]', '(4500, 5000]', '(5000, 5500]', '(5500, 6000]'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : None
                              , 'annotations' : [dict(x=0, y=190, text=f'최소 점수 {score_df['norm_Gr_Liv_Area'].min()}점 부여', showarrow=False, font=dict(size=9,color='gray'))
                                                  , dict(x=7, y=190, text=f'최대 점수 {score_df['norm_Gr_Liv_Area'].max()}점 부여', showarrow=False, font=dict(size=9,color='gray'))]
                              }]
                        ),
                dict( label='리모델링 연도', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False]}
                            , {'title' : dict(text='군집마다 리모델링 (없으면 건축연도) 연도별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                               ,'xaxis' : dict(title = dict(text='리모델링 연도 (리모델링 연도가 최근일 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=list(g8['Year_Remod_Add'].unique()))
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                               , 'shapes' : None
                               , 'annotations' : [dict(x=1952, y=130, text=f'최소 점수 {score_df['norm_Year_Remod_Add'].min()}점 부여', showarrow=False, font=dict(size=9,color='gray'))
                                                  , dict(x=2007, y=130, text=f'최대 점수 {score_df['norm_Year_Remod_Add'].max()}점 부여', showarrow=False, font=dict(size=9,color='gray'))]
                              }]
                        ),
                dict( label='진입 도로 유형', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 진입도로 유형별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='진입 도로 유형 (진입도로가 포장도로인 집을 선호함)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['Dirt_Gravel', 'Partial_Pavement', 'Paved'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : [dict(type='line',x0=1.5, x1=1.5, y0=g6['counts'].min()-1, y1=g6['counts'].max()+10, line=dict(color='gray',width=2, dash='dash'))]
                              , 'annotations' : [dict(x=2, y=300, text='포장도로를 선호함',showarrow=False, font=dict(size=9,color='gray'))]}
                            ]
                        ),
                dict( label='울타리 유형', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False]}
                            ,{'title' : dict(text='군집마다 울타리 유형별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='울타리 유형 (최소한의 프라이버시를 지켜주는 울타리를 선호함)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['No_Fence', 'Minimum_Wood_Wire', 'Good_Wood', 'Minimum_Privacy', 'Good_Privacy'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : [dict(type='line',x0=2.5, x1=2.5, y0=g7['counts'].min()-1, y1=g7['counts'].max()+10, line=dict(color='gray',width=2, dash='dash'))]
                              , 'annotations' : [dict(x=3.5, y=62, text='최소한의 프라이버시를 선호함', showarrow=False, font=dict(size=9,color='gray'))]}
                            ]
                        ),
                dict( label='점수 높은 집', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True]}
                            ,{'title' : dict(text='점수가 높은 집', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title = dict(text='점수가 가장 높은 집 인덱스',font=dict(size=14,color='black')),categoryorder='array',categoryarray=list(g10['Unnamed: 0'].astype('str')))
                              , 'yaxis' : dict(title=dict(text='총점', font=dict(size=14,color='black')))
                              , 'shapes' : None
                              , 'annotations' :[dict(x=0.5, y=5.5, text='(가장 좋은 집 : 최대 8점)',showarrow=False, font=dict(size=9,color='gray'))]}
                            ]
                        ),
             ]
        )
    ]
)




# html로 저장하기
fig.write_html('code/plotly2.html', full_html=True)





# --------------------------

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')



eda_df = pd.read_csv('./data/eda_house.csv')
g1 = eda_df[eda_df['cluster']!= -1].groupby(['Bedroom_AbvGr','cluster'], as_index=False).agg(counts=('Bedroom_AbvGr','count'))


fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title='shapes type="line", dash="solid", layer="above"',height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above")]
)
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title='shapes type="line", dash="solid", layer="above" \nx0=3, x1=3, y0=df['col'].min()-1, y1=df['col'].max()+10',height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above")]
)
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type="line", dash="solid", layer="above" \nx0=3, x1=3, y0=df['col'].min()-1, y1=df['col'].max()+10",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above")]
)
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='line', dash='solid', layer='above' \nx0=3, x1=3, y0=df['col'].min()-1, y1=df['col'].max()+10",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above")]
)
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='line', dash='solid', layer='above'",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above")]
)
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='line', dash='solid', layer='below'",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="below")]
)
g1.index
g1
g1['Bedroom_AbvGr'].min()
g1['Bedroom_AbvGr'].max()
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='line', dash='solid'",height=400, width=600,
    shapes=[dict(type="line", x0=g1['Bedroom_AbvGr'].min(), x1=g1['Bedroom_AbvGr'].max(), y0=50, y1=50, line=dict(color="red", width=1))]
)

fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="x0=df['col'].min()-1, x1=df['col'].max(), y0=50, y1=50",height=400, width=600,
    shapes=[dict(type="line", x0=g1['Bedroom_AbvGr'].min()-1, x1=g1['Bedroom_AbvGr'].max(), y0=50, y1=50, line=dict(color="red", width=1))]
)





fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="x0=3, x1=3, y0=df['col'].min()-1, y1=df['col'].max()+10",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1))]
)






fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="x0=3, x1=5, y0=df['col'].min()-1, y1=df['col'].max()+10",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=5, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1))]
)




fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="dash='dot'",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='dot'))]
)



fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="dash='longdash'",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='longdash'))]
)



"
fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="dash='dashdot'",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='dashdot'))]
)


fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="dash='dash'",height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='dash'))]
)




fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='rect', fillcolor='red'",height=400, width=600,
    shapes=[dict(type="rect", x0=3, x1=4, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), fillcolor='red')]
)



fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='rect', dash='dash'",height=400, width=600,
    shapes=[dict(type="rect", x0=3, x1=4, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='dash'))]
)




fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='circle', dash='dash'",height=400, width=600,
    shapes=[dict(type="circle", x0=3, x1=4, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='dash'))]
)



fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='circle', fillcolor='red'",height=400, width=600,
    shapes=[dict(type="circle", x0=3, x1=4, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), fillcolor='red')]
)



fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title="shapes type='path', dash='dash'",height=400, width=600,
    shapes=[dict(type="path", x0=3, x1=4, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1, dash='dash'))]
)



fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title='shapes=[dict(), dict()]',height=400, width=600,
    shapes=[dict(type="line", x0=3, x1=3, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above"),
            dict(type="line", x0=5, x1=5, y0=g1['counts'].min()-1, y1=g1['counts'].max()+10, line=dict(color="red", width=1), layer="above")],
    xaxis=dict(categoryorder='array',categoryarray=['0','1','2','3','4','5','6'])
)




fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title='annotations=[dict(), dict()]',height=400, width=600,
    annotations=[dict(x=0.5, y=150, text='중요1'),
            dict(x=4.5, y=150, text='중요2', showarrow=False)],
    xaxis=dict(categoryorder='array',categoryarray=['0','1','2','3','4','5','6'])
)






fig = go.Figure()


# 두 개의 그래프 trace
fig.add_trace(go.Scatter(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Scatter(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.add_trace(go.Bar(x=g2[g2['cluster']==0]['TotRms_AbvGrd'].astype('str') , y=g2[g2['cluster']==0]['counts']
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g2[g2['cluster']==2]['TotRms_AbvGrd'].astype('str') , y=g2[g2['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g2[g2['cluster']==1]['TotRms_AbvGrd'].astype('str') , y=g2[g2['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))


fig.update_layout(
    title='shapes=[dict(), dict()]',height=400, width=600,
)

fig.update_layout(
    autosize=True,
    updatemenus=[
        dict(type='buttons',
             buttons=[
                dict( label='침실 수', method ='update', 
                      args=[{'visible':[True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 침실 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['0','1','2','3','4','5','6'])
                              , 'shapes' : [dict(type='line',x0=0.5,x1=0.5,y0=g1['counts'].min()-1, y1=g1['counts'].max()+10,line=dict(color='red',width=2,dash='dash'))]}
                            ]
                        ),
                dict( label='방 수', method ='update', 
                      args=[{'visible':[False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 방 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['3','4','5','6','7','8','9','10','11','12'])
                              , 'shapes' : [dict(type='line',x0=1.5,x1=1.5,y0=g2['counts'].min()-1, y1=g2['counts'].max()+10,line=dict(color='red',width=2,dash='dash'))]}
                            ]
                        )])]
        )




fig = go.Figure()

# 두 개의 그래프 trace
fig.add_trace(go.Bar(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.update_layout(title='큰 제목', xaxis_title='x축 제목', yaxis_title='y축 제목')






fig = go.Figure()

# 두 개의 그래프 trace
fig.add_trace(go.Bar(x=g1[g1['cluster']==0]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==0]['counts'] 
                ,name="군집0", showlegend=True, marker=dict(color='darkred')))
fig.add_trace(go.Bar(x=g1[g1['cluster']==2]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==2]['counts']
                     ,name="군집2", showlegend=True, marker=dict(color='purple')))
fig.add_trace(go.Bar(x=g1[g1['cluster']==1]['Bedroom_AbvGr'].astype('str') , y=g1[g1['cluster']==1]['counts']
                     ,name="군집1", showlegend=True, marker=dict(color='darkblue')))

fig.update_layout(
    autosize=True,
    updatemenus=[
        dict(type='buttons',
             #x=-0.1,
             y=0,
             yanchor='middle',
             buttons=[
                dict( label='침실 수', method ='update', 
                      args=[{'visible':[True, True,True]}
                            ,{'title' : dict(text='군집마다 침실 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(title=dict(text='침실 수 (침실이 많을 수록 높은 점수 부여)',font=dict(size=14,color='black')),categoryorder='array',categoryarray=['0','1','2','3','4','5','6'])
                              , 'yaxis' : dict(title=dict(text='가구 수', font=dict(size=14,color='black')))
                              , 'shapes' : bed_shape
                              , 'annotations' : bed_annotation}
                            ]
                        )
                                     ]
        )
    ]
)


# html로 저장하기
fig.write_html('code/plotly2.html', full_html=True)