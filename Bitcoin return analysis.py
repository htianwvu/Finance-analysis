# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:50:24 2020

@author: htian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

bitcoin_speculation = 1000 # Speculating $1000 on bitcoin
returns = 0.35 # Assuming 35% returns
# Creating an empty table
fv_table = np.zeros((30,4))
fv_table = pd.DataFrame(fv_table)
fv_table.columns = ['Year', 'beg_val', 'ret', 'end_val']
fv_table['Year'] = np.arange(1,31)
# Calculating the first row values
fv_table.iloc[0,1] = bitcoin_speculation
fv_table.iloc[0,2] = returns * bitcoin_speculation
fv_table.iloc[0,3] = fv_table.iloc[0,1] + fv_table.iloc[0,2]
# For loop
for i in range(1,30):
    fv_table.iloc[i,1] = fv_table.iloc[(i-1),3]
    fv_table.iloc[i,2] = fv_table.iloc[i,1] * returns
    fv_table.iloc[i,3] = fv_table.iloc[i,1] + fv_table.iloc[i,2]
    
print(fv_table.tail().round(2))

