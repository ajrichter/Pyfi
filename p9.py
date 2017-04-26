# Using Machine Learning to see how companies are correlated
# What if we use pricing to see how movement of other companies might give us an edge?
# Features: Define Something
# Labels: A Target Buy/Sell/Hold
# Based on the question within 7 days did price go up? or fall? or neither
import numpy as np
import pandas as pd
import pickle
# Per company basis. Take in data from all companies
# First Mover and Lagging companies folllow
# Looking for a few days lag where a company is correlated a day
# or two after another company
def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df

process_data_for_labels('XOM')
