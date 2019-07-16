# %% [markdown]

# 预测自行车流量

# !curl -o fremont_hourly.csv https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD


'''
http://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND
https://www.ncei.noaa.gov/orders/cdo/1804932.csv
'''

# %%

%matplotlib inline
import os
import pandas as pd

print(os.getcwd())
path = './usiege/Python/projects/handbook'
counts = pd.read_csv(path + "/dataset/fremont_hourly.csv",
                     index_col='Date', parse_dates=True)
weather = pd.read_csv(path + "/dataset/1804932.csv",
                      index_col='DATE', parse_dates=True)
# weather.head()

#%%

daily = counts.resample('d', how='sum')
daily['Total'] = daily.sum(axis=1)
daily = daily[['Total']]
daily

#%%

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in range(7):
    daily[days[i]] = (daily.index.dayofweek == i).astype(float)
daily

#%%

from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012', '2016')
daily = daily.join(pd.Series(1, index=holidays, name='holiday'))
daily['holiday'].fillna(0, inplace=True)
daily

#%%
## code data error