# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:27:23 2020

@author: htian
"""

import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import yfinance as yf