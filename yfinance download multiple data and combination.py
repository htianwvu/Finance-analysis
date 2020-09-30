# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:51:33 2020

@author: htian
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

aapl = yf.download("AAPL", start = "2017-01-01", end = "2018-03-01")

print(aapl.head())

aapl["Adj Close"].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted Price")
plt.title("Apple price data")
plt.show()

tickers = ["AAPL", "MSFT", "AMZN", "K", "O"]
prices = yf.download (tickers, start = "2017-01-01", end = "2023-01-15")
print(prices.head())


prices["Adj Close"].head()

prices["Adj Close"].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted Price")
plt.title("All stocks price data")
plt.show()