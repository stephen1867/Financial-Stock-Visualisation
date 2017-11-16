import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
style.use('ggplot')

df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)

df['movavg'] = df['Open'].rolling(window=100).mean()                        # simple moving average
df.dropna(inplace=True)

df['expmov'] = pd.ewma(df['Open'],span=100,freq='D',ignore_na=True)         # exponential moving average using pandas

ax1 = plt.subplot2grid((6,1), (0,-1), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

ax1.plot(df.index,df.expmov)
ax1.plot(df.index,df.movavg)
ax1.plot(df.index,df.Open)                                                  # plots the open price
ax1.set_ylabel('Price (USD)')



ax2.plot(df.index,df.Volume)

ax2.set_ylabel('Volume')

plt.show()
