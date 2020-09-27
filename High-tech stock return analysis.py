import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# name the stock
tickers = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]
multpl_stocks = yf.download(tickers, start = "2013-01-01", end = "2018-03-01")

# chart multiple stocks

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(multpl_stocks['Adj Close']['AMZN'])
ax1.set_title("Amazon")
ax2.plot(multpl_stocks['Adj Close']['AAPL'])
ax2.set_title("Apple")
ax3.plot(multpl_stocks['Adj Close']['FB'])
ax3.set_title("Facebook")
ax4.plot(multpl_stocks['Adj Close']['NFLX'])
ax4.set_title("Netflix")
ax5.plot(multpl_stocks['Adj Close']['GOOG'])
ax5.set_title("Google")
plt.tight_layout()
plt.show()

# calculate multiple stocks and then plot out

multpl_stock_daily_returns = multpl_stocks['Adj Close'].pct_change()
multpl_stock_monthly_returns = multpl_stocks['Adj Close'].resample('M').ffill().pct_change()

fig = plt.figure()
(multpl_stock_monthly_returns + 1).cumprod().plot()
plt.show()

# process statistical data
print(multpl_stock_monthly_returns.mean())
print(multpl_stock_monthly_returns.std())

#correlation and covariance 

print(multpl_stock_monthly_returns.corr())
print(multpl_stock_monthly_returns.cov())

