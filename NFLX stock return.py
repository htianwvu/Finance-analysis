import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# name the stock
tickers = ['NFLX']

# generate data
netflix09272020= yf.download(tickers,start = '2009-09-01',
                             end = '2022-02-01')
#netflix09272020.head()
netflix09272020['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("Netflix Price data")
plt.show()

# calculate the daily and month return
netflix_daily_returns = netflix09272020['Adj Close'].pct_change()
netflix_monthly_returns = netflix09272020['Adj Close'].resample('M').ffill().pct_change()
netflix_daily_returns
netflix_monthly_returns 

# plot daily return

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(netflix_daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("Netflix daily returns data")
plt.show()

# plot monthly return

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(netflix_monthly_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("Netflix monthly returns data")
plt.show()


# plot histogram to see the vibration in more details

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
netflix_daily_returns.plot.hist(bins = 60)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("Netflix daily returns data")
ax1.text(-0.35,200,"Extreme Low\nreturns")
ax1.text(0.25,200,"Extreme High\nreturns")
plt.show()

# calcualte the cumulative return  cumprod() for netflix
# plot the cumulative returns

netflix_cum_returns = (netflix_daily_returns + 1).cumprod()
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
netflix_cum_returns.plot()
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth of $1 investment")
ax1.set_title("Netflix daily cumulative returns data")
plt.show()

# replot with monthly return

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
netflix_cum_returns = (netflix_monthly_returns + 1).cumprod()
ax1.plot(netflix_cum_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth of $1 investment")
ax1.set_title("Netflix Monthly cumulative returns data")
plt.show()









