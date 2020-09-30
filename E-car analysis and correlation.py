# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:56:45 2020

@author: htian
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# name the stock
tickers = ["TSLA", "NIO", "KCAC", "XPEV","DPHC"]
multpl_stocks = yf.download(tickers, start = "2020-01-01", end = "2023-12-31")

# chart multiple stocks

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(multpl_stocks['Adj Close']['TSLA'])
ax1.set_title("TSLA")
ax2.plot(multpl_stocks['Adj Close']['NIO'])
ax2.set_title("NIO")
ax3.plot(multpl_stocks['Adj Close']['KCAC'])
ax3.set_title("KCAC")
ax4.plot(multpl_stocks['Adj Close']['XPEV'])
ax4.set_title("XPEV")
ax4.plot(multpl_stocks['Adj Close']['XPEV'])
ax4.set_title("DPHC")
plt.tight_layout()
plt.show()

# calculate multiple stocks and then plot out

multpl_stock_daily_returns = multpl_stocks['Adj Close'].pct_change()
multpl_stock_monthly_returns = multpl_stocks['Adj Close'].resample('M').ffill().pct_change()

fig = plt.figure()
(multpl_stock_daily_returns + 1).cumprod().plot()
plt.show()

# process statistical data
print(multpl_stock_daily_returns.mean())
print(multpl_stock_daily_returns.std())

#correlation and covariance 

print(multpl_stock_daily_returns.corr())
print(multpl_stock_daily_returns.cov())

