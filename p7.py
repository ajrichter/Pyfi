import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def save_sp500_tickers() :
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)


    return tickers

# throw in time.sleep if you seem to be getting throttled
def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
            with open("sp500tickers.pickle","rb") as f:
                    tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)

    # to test say tickers [:25] or tickers for all
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker.replace(".","-"), 'yahoo',start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))



def compile_data():
    with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count,ticker in enumerate(tickers):
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
            df.set_index('Date', inplace=True)

            df.rename(columns = {'Adj Close':ticker}, inplace=True)
            df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

            if main_df.empty:
                    main_df = df
            else:
                    main_df = main_df.join(df, how='outer')

            if count % 10 ==0:
                    print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

# not running this again as it takes ~20 min
# get_data_from_yahoo()
compile_data()
