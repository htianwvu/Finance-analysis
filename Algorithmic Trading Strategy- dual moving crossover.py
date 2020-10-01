# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:40:28 2020

@author: htian
"""
# descriptionL this program uses the dual moving average crossover to determine
#when to buy and sell stock

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

# load the data

tickers = ["AAPL"]

aapl = yf.download(tickers, start = "2010-03-20", end = "2023-01-01")

print(aapl.head())

# visualize the data

plt.figure(figsize=(12.5, 4.5))
plt.plot(aapl['Open'],label = 'AAPL')
plt.title('Apple Open Price Hostory')
plt.xlabel("All time long")
plt.ylabel("Open Price $")
plt.legend(loc='upper left')
plt.show()

# create the simple moving average with a 30 day window
SMA30 = pd.DataFrame()
SMA30['Open'] = aapl[('Open')].rolling(window= 30).mean()
SMA30

# create another simple moving average with a 100 day window

SMA100 = pd.DataFrame()
SMA100['Open'] = aapl[('Open')].rolling(window= 100).mean()
SMA100


# visualize the data

plt.figure(figsize=(12.5, 4.5))
plt.plot(aapl['Open'],label = 'AAPL')
plt.plot(SMA30['Open'],label = 'SMA30')
plt.plot(SMA100['Open'],label = 'SMA100')
plt.title('Apple Open Price Hostory')
plt.xlabel("All time long")
plt.ylabel("Open Price $")
plt.legend(loc='upper left')
plt.show()

# create a new data frame to store all the data
data = pd.DataFrame()
data['aapl'] = aapl[('Open')]
data['SMA30'] = SMA30['Open']
data['SMA100'] = SMA100['Open']
data

# # create a function to signal when to buy and sell the asset
def buy_sell(data):
    sigPriceBuy = []
    sigPricesell = []
    flag = -1
    for i in range(len(data)):
        if data['SMA30'][i]> data['SMA100'][i]:
                if flag != 1:
                    sigPriceBuy.append(data['aapl'][i])
                    sigPricesell.append(np.nan)
                    flag = 1
                else:
                    sigPriceBuy.append(np.nan)
                    sigPricesell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPricesell.append(data['aapl'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPricesell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPricesell.append(np.nan)

    return (sigPriceBuy,sigPricesell)
            
# store the buy and sell data intor a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]
#show the data
print(data)

# visualize the data and strategry to buy and sell the stock
plt.figure(figsize=(12.6, 4.6))
plt.plot(data['aapl'],label = 'AAPL Open', alpha = 0.35)
plt.plot(data['SMA30'], label = 'SMA30', alpha = 0.35)
plt.plot(data['SMA100'], label = 'SMA100', alpha = 0.35)
plt.title('Apple Open Price Hostory')
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', 
            marker = "^", color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = "Sell",
                             marker = "v", color = 'red')
                            
plt.title('Apple Open. History buy and sell signals')        
plt.xlabel('all time')      
plt.ylabel('Open price $') 
      
plt.legend(loc='upper left')
plt.show()    
                                            