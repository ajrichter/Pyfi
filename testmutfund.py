# I am going to test getting example mut fund data
import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import csv

style.use('ggplot')

with open('mutual.csv', 'rb') as cf:
        spamreader = csv.reader(cf, delimiter=',', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
