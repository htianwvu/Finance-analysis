import pandas as pd
import yfinance as yf


# name the stock
tickers = ['DFEN', 'WMT', 'QQQ']

# generate data
DFEN09272020= yf.download(tickers,start = '2002-09-01', end = '2022-02-01')
DFEN09272020.info()

# export to excel 
DFEN09272020.to_excel('DFEN09272020.xls')
