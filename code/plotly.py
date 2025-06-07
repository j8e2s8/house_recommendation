import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

os.chdir('c:/Users/USER/Documents/D/LS_bigdataschool_3/house_recommendation')



eda_df = pd.read_csv('./data/eda_house.csv')


g1 = eda_df[eda_df['cluster']!= -1].groupby(['Bedroom_AbvGr','cluster'], as_index=False).agg(counts=('Bedroom_AbvGr','count'))
g2 = eda_df[eda_df['cluster']!= -1].groupby(['TotRms_AbvGrd','cluster'], as_index=False).agg(counts=('TotRms_AbvGrd','count'))
g3 = eda_df[eda_df['cluster']!= -1].groupby(['Garage_Cars','cluster'], as_index=False).agg(counts=('Garage_Cars','count'))
g4 = eda_df[eda_df['cluster']!= -1].groupby(['Overall_Cond','cluster'], as_index=False).agg(counts=('Overall_Cond','count'))
g5 = eda_df[eda_df['cluster']!= -1].groupby(['Exter_Cond','cluster'], as_index=False).agg(counts=('Exter_Cond','count'))
g6 = eda_df[eda_df['cluster']!= -1].groupby(['Paved_Drive','cluster'], as_index=False).agg(counts=('Paved_Drive','count'))
g7 = eda_df[eda_df['cluster']!= -1].groupby(['Fence','cluster'], as_index=False).agg(counts=('Fence','count'))
g8 = eda_df[eda_df['cluster']!= -1].groupby(['Year_Remod_Add','cluster'], as_index=False).agg(counts=('Year_Remod_Add','count'))
pivot_df = g8.pivot_table(index='Year_Remod_Add',columns='cluster',values='counts')

pivot_df.columns


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



fig.add_trace(go.Scatter(x=pivot_df.index , y=pivot_df[0]
                , mode='lines+markers' ,marker=dict(size=3, color='darkred'), line=dict(width=1),name="군집0", showlegend=True))
fig.add_trace(go.Scatter(x=pivot_df.index , y=pivot_df[2]
                    , mode='lines+markers' ,marker=dict(size=3, color='purple'), line=dict(width=1),name="군집1", showlegend=True))
fig.add_trace(go.Scatter(x=pivot_df.index , y=pivot_df[1]
                    , mode='lines+markers' ,marker=dict(size=3, color='darkblue'), line=dict(width=1),name="군집2", showlegend=True))


fig.update_layout(
    margin=dict(l=100, r=100, t=100) 
)

fig.update_layout(
    autosize=True,
    updatemenus=[
        dict(type='buttons',
             buttons=[
                dict( label='침실 수', method ='update', 
                      args=[{'visible':[True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 침실 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['0','1','2','3','4','5','6'])}
                            ]
                        ),
                dict( label='방 수', method ='update', 
                      args=[{'visible':[False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 방 수별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['3','4','5','6','7','8','9','10','11','12'])}
                            ]
                        ),
                dict( label='차 수용량', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 차 수용량별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['0','1','2','3','4'])}
                            ]
                        ),
                dict( label='전반적인 상태', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 전반적인 상태별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['Very_Poor','Poor','Fair','Below_Average','Average','Above_Average', 'Good','Very_Good','Excellent'])}
                            ]
                        ),
                dict( label='외관 자재 상태', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 외관 자재별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['Fair','Typical','Good','Excellent'])}
                            ]
                        ),
                dict( label='진입 도로 유형', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False,False,False,False]}
                            ,{'title' : dict(text='군집마다 진입도로 유형별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['Dirt_Gravel', 'Partial_Pavement', 'Paved'])}
                            ]
                        ),
                dict( label='울타리 유형', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True,False,False,False]}
                            ,{'title' : dict(text='군집마다 울타리 유형별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))
                              ,'xaxis' : dict(categoryorder='array',categoryarray=['No_Fence', 'Minimum_Wood_Wire', 'Good_Wood', 'Minimum_Privacy', 'Good_Privacy'])}
                            ]
                        ),
                dict( label='리모델링 연도', method ='update', 
                      args=[{'visible':[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True, True,True]}
                            , {'title' : dict(text='군집마다 리모델링 연도별 가구 수', x=0.5,xanchor='center',font=dict(size=20,color='black'))}]
                        )
             ]
        )
    ]
)



# html로 저장하기
fig.write_html('./code/plotly.html', full_html=True)

