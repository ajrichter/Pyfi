# code copied from p1.py
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')
# data frame
df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)
#
# today's 100 moving average
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)
#print(df.head())
print(df.tail())

# Graph with PURE MatPlotLib
ax1 = plt.subplot2grid((6, 1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot()
ax2.plot()

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
