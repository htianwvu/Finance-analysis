# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:29:07 2020

@author: htian
"""


# this program is to predict stock price by using machine learning models
# install the dependencies

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import yfinance as yf

tickers = ["NIO"]

df = yf.download(tickers, start = "2010-03-20", end = "2023-01-01")

print(df.head())

# get the adjusted close price
df = df[["Adj Close"]]
# take a look at the new data
print(df.head())

# program a variable for predicting "n" days out in the future

n= 3  # this is adjustable
forcast_out = n

# create another column (the target or denpendent variable ) shifted 'n; units up
df['Prediction'] = df[['Adj Close']].shift(-n)
#print out the new data set
print(df.head())

print(df.tail())

### create the independent data set XXX
# convert the dataframe to a numply array

x = np.array(df.drop(['Prediction'],1))
## remove the last 'n' rows
x = x[:-n]

print(x)

## Create the dependent dataset y###

# convert the dataframe to a numpy array (all of the values including the NaN's)

y = np.array(df["Prediction"])

# get all of the y values except the last 'n" rows
y = y[:-n]
print(y)

#split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2)

# creat and train the support vector machine (Regressor)
svr_rbf = SVR(kernel='rbf', C= 1e3,gamma = 0.1)
svr_rbf.fit(x_train, y_train)

## testing model: score returns the coefficient of determination R^2 of 
#the prediction score close to 1.0 
svr_confidence = svr_rbf.score(x_test, y_test)
print('svr_confidence is', svr_confidence )

# create an train the linear regression model
lr = LinearRegression()
# train the  model
lr.fit(x_train, y_train)

## testing model: score returns the coefficient of determination R^2 of 
#the prediction score close to 1.0 

lr_confidence = lr.score(x_test, y_test)
print('lr_confidence is', lr_confidence )

## create the value of our prediction
## set x-forcast equal to the last 30 roriginal data set from Adj. close column

x_forcast = np.array(df.drop(['Prediction'],1)) [-forcast_out:]
print(x_forcast)

## take look the prediction for next "n" days
# print linear regression model prediction for the next 'n' days
lr_prediction = lr.predict(x_forcast)
print(lr_prediction)

# print support vestor regreesion model prediction for the next 'n' days
svr_prediction = svr_rbf.predict(x_forcast)
print(svr_prediction)

