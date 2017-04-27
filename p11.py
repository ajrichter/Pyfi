# Mapping tutorial on pyprogramming.net
import numpy as np
import pandas as pd
import pickle
from

def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df

def buy_sell_hold(*args):
        cols = [c for c in args]
        requirement = 0.02
        # means 2 % in 7 days
        for col in cols:
            if col > requirement:
                return 1
            if col < -requirement:
                return -1
        return 0

def extract_featureset(ticker):
        tickers, df = process_data_for_labels(ticker)

        df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
                                                                                df['{}_1d'.format(ticker)],
                                                                                df['{}_2d'.format(ticker)],
                                                                                df['{}_3d'.format(ticker)],
                                                                                df['{}_4d'.format(ticker)],
                                                                                df['{}_5d'.format(ticker)],
                                                                                df['{}_6d'.format(ticker)],
                                                                                df['{}_7d'.format(ticker)],
                                                                                ))
        vals = df['{}_target'.format(ticker)].values.tolist()
        string_vals = [str(i) for i in vals]
        print('Data spread:', Counter(str_vals))
