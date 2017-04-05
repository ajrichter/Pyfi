import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
#start = dt.datetime(2000,1,1)
#end = dt.datetime(2016,12,31)
#df = web.DataReader('TSLA', 'yahoo', start, end)
#print(df.tail(6))
#df.to_csv('tesla.csv')
df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)
#print(df.head())

print("Testing Open Prices")
print(df[['Open' , 'High']].head())
df['Adj Close'].plot()
plt.show()
