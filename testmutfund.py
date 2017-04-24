# I am going to test getting example mut fund data
import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2017, 4, 1)
end = dt.datetime(2017, 4, 20)

print("JDST")
jd = web.DataReader("JDST", 'yahoo', start, end)
print(jd[['Adj Close']].tail())
print("JNUG")
ju = web.DataReader("JNUG", 'yahoo', start, end)
print(ju[['Adj Close']].tail())
print("VFFVX")
v55 = web.DataReader("VFFVX", 'yahoo', start, end)
print(v55[['Adj Close']].tail())
print("SPY")
spy = web.DataReader("SPY", 'yahoo', start, end)
print(spy[['Adj Close']].tail())
