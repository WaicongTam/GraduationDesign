import numpy as np
import pandas as pd
from preprocess import data_preprocessed as dt
from preprocess import direction

period_monthly_average=pd.DataFrame(columns=list(range(1,13)),index=[0])
height_monthly_average=pd.DataFrame(columns=list(range(1,13)),index=[0])
wavedir_monthly_average=pd.DataFrame(columns=list(range(1,13)),index=[0,1])
ws_monthly_average=pd.DataFrame(columns=list(range(1,13)),index=[0])
winddir_monthly_average=pd.DataFrame(columns=list(range(1,13)),index=[0])


for i in list(range(0,12)):
    month_data=dt.loc[dt.MONTH==i,:]
    period_monthly_average.iloc[0,i]=month_data.mean(axis=0)['Tbar']
    height_monthly_average.iloc[0,i]=month_data.mean(axis=0)['HS']
    wavedir_monthly_average.iloc[0,i]=month_data.mean(axis=0)['DMDIR']
    ws_monthly_average.iloc[0,i]=month_data.mean(axis=0)['WS']
    winddir_monthly_average.iloc[0,i]=month_data.mean(axis=0)['WD']
    
for i in range(12):
    wavedir_monthly_average.iloc[1,i]=direction(wavedir_monthly_average.iloc[0,i])

with pd.ExcelWriter('month_average.xlsx') as writer:
    period_monthly_average.to_excel(writer,sheet_name='Tbar')
    height_monthly_average.to_excel(writer,sheet_name='HS')
    wavedir_monthly_average.to_excel(writer,sheet_name='WD')
    ws_monthly_average.to_excel(writer,sheet_name='WS')
    