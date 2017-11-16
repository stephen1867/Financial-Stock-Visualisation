import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
style.use('ggplot')
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

df = pd.read_csv('tsla.csv',parse_dates=True, index_col=0)      # Reads the csv file which the data is stored

df_ohlc = df['Open'].resample('10D').ohlc()                  # Creates new column in the dataframe which takes a 10 day moving average of the data
df_volume = df['Volume'].resample('10D').sum()              # Does the same for the volume

df_ohlc = df_ohlc.reset_index()                              # resets the time index so it can be used in the candle stick chart

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)                  #plotting
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

ax1.xaxis_date()                                                            # formatting/plotting
ax1.set_ylabel('Price (USD)')
ax2.set_ylabel('Volume')
ax1.set_title('Price history of TSLA')


candlestick_ohlc(ax1,df_ohlc.values,width=2, colorup='g')                   # candlestick call


ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0) #takes out missing information e.g weekend data

plt.show()
