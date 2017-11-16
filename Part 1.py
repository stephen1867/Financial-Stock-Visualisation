import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use('ggplot')                                                 # Changes graph to a different style
# defines what time period to look at for a particular stock
start = dt.datetime(2015,1,1)                                #Specifies the start and end dates to look at the stock at
end = dt.date.today()

# creates a dataframe which reads information from google finance
ticker = 'TSLA'
df = web.DataReader(ticker,"google",start,end)


df.to_csv('TSLA.csv')

df = pd.read_csv('tsla.csv',parse_dates=True, index_col=0)
variability = df['High'] - df['Low']
ax = df.Open.plot()
ax.set_xlabel('Dates')
ax.set_ylabel('Price (USD)')

print('hi')
plt.show()

