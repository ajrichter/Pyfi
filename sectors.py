import bs4 as bs
from collections import Counter
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
from sklearn import svm, neighbors, model_selection
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

style.use('ggplot')
# What sector a ticker is in
sectors = {}
# All stocks in a sector
groups = {}
# list of sp500 ETFS
etfs = []


def save_sectors():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
        sector = row.findAll('td')[3].text
        sectors[ticker] = sector
        if sector in groups:
            groups[sector].append(ticker)
        else:
            groups[sector] = [ticker]

    for gs in sorted(groups.keys()):
        print(gs, "is", groups[gs])
        print()

    print('UPS:', sectors['UPS'])

    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    pickle.dump(sectors, open("spSectors.pickle","wb"))
    pickle.dump(groups, open("spGroups.pickle","wb"))

    return tickers

# All tickers, their corresponding sectors, and all the tickers in a sector have been pickled
# Weight by MktCap. Then show changes over time. Right?

def get_data_from_yahoo(reload_sp500=False):

    if reload_sp500:
        tickers = save_sectors()
    else:
        sectors = pickle.load(open("spSectors.pickle","rb"))
        groups = pickle.load(open("spGroups.pickle","rb"))
        tickers = pickle.load(open("sp500tickers.pickle","rb"))

    if not os.path.exists('sector_dfs'):
        os.makedirs('sector_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2017, 4, 30)

    for ticker in tickers:
        # just in case your connection breaks, we'd like to save our progress!
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, "yahoo", start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
            print('Downloaded {}'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

def get_SP500():
    # SPDR
    etfs.append('SPY')
    # Blackrock
    etfs.append('IVV')
    # Vanguard
    etfs.append('VOO')
    # Schwab MUTF
    etfs.append('SWPPX')

    start = dt.datetime(2007, 1, 1)
    end = dt.datetime(2017, 5, 10)

    for e in etfs:
        eval = web.DataReader(e, 'yahoo', start, end)
        print(e, jd[['Adj Close']].tail())

get_SP500()
