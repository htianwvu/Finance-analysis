# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:57:35 2020

@author: htian
"""

# comparision  portfolio return

#Aggregate Bonds ETF (BND) 10%
#Small Cap ETF (VB) 20%
#Developed markets ETF (VEA) 25%
#S&P 500 ETF (VOO) 25%
# Emerging Markets ETF (VWO) 20%


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

symbols = ['ARKK','QQQ', 'SOXX', 'ONLN']

price_data = yf.download(symbols, start = '2020-01-01', end = '2023-03-01')

print(price_data.head())

price_data = price_data['Adj Close']
print(price_data.head())

#Our weight

w = [0.25, 0.25,0.25,0.25]
print(sum(w))

# calculate the asset returns in our portfolio.
ret_data = price_data.pct_change()[1:]
print(ret_data.head())

#calculate the weighted returns of our assets.

weighted_returns = (w * ret_data)
print(weighted_returns.head())


#the portfolio returns are simply the sum of the weighted returns of the assets.

port_ret = weighted_returns.sum(axis=1)
print(port_ret)
# axis =1 tells pandas we want to add
# the rows



##########################################
##calculate cumulative returns we need to use the cumprod() function.
cumulative_ret = (port_ret + 1).cumprod()
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(cumulative_ret)
ax1.set_xlabel('Date')
ax1.set_ylabel("Cumulative Returns")
ax1.set_title("Portfolio Cumulative Returns")
plt.show();





fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.hist(port_ret, bins = 60)
ax1.set_xlabel('Portfolio returns')
ax1.set_ylabel("Freq")
ax1.set_title("Portfolio Returns calculated manually")
plt.show(); 

#Optimize return by chaning the weight

wts_table = pd.DataFrame({'symbol':symbols,
                          'wts':[0.25,0.25,0.2,0.8]})
print(wts_table.head())


# transform our returns data into a tidy data. 
#reset the index and make the Date index into a separate column

ret_data_tidy = pd.melt(ret_data.reset_index(),
        id_vars='Date',
        var_name='symbol',
        value_name='ret')
        
print(ret_data_tidy.head())

#merge our data by symbols

ret_data_tidy_wts = pd.merge(ret_data_tidy,wts_table,on="symbol")
print(ret_data_tidy_wts.head())

ret_data_tidy_wts['wt_returns'] = ret_data_tidy_wts['ret'] * ret_data_tidy_wts['wts'] 
print(ret_data_tidy_wts.head())

#group our dataframe by date to calculate the daily returns on our portfolio.
port_ret_tidy = ret_data_tidy_wts.groupby("Date").sum()['wt_returns']
print(port_ret_tidy.head())


# plot other histograms

# manual return
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.hist(port_ret, bins = 60) # manually calculated returns
ax1.set_xlabel('Portfolio returns')
ax1.set_ylabel("Freq")
ax1.set_title("Portfolio Returns calculated manually")
plt.show();

#tidy return

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.hist(port_ret_tidy, bins = 60) # Tidy returns
ax1.set_xlabel('Portfolio returns')
ax1.set_ylabel("Freq")
ax1.set_title("Portfolio Returns calculated in Tidy format")
plt.show();

#Portfolio mean and standard deviation

mean_ret = port_ret.mean()
std_returns = port_ret.std()
print(mean_ret)

print(std_returns)


