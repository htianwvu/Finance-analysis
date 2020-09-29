# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:26:39 2020

@author: htian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


#Yearly salary $36000 (3000 per month)
#Yearly deposit $3600
#Stock Returns 7.5%
#Both save for the same duration 20 year, but their timing is different.
#Tom saves from age 20 to 40
#Jerry save from age 50 to 70
#They both will retire at age 70

# Jerry's Table
returns = 0.075
annual_deposit = 3600  
# Creating the empty table
fv_table = np.zeros((50,5))
fv_table = pd.DataFrame(fv_table)
fv_table.columns = ['Year', 'beg_val', 'deposit', 'ret', 'end_val']
fv_table['Year'] = np.arange(1,51)
# Calculating the first row values
fv_table.iloc[0,2] = annual_deposit
fv_table.iloc[0,3] = annual_deposit * returns
fv_table.iloc[0,4] = fv_table.iloc[0,3] + fv_table.iloc[0,2]
# Running the for loop for first phase
for i in range(1,20):
    fv_table.iloc[i,1] = fv_table.iloc[(i-1),4]
    fv_table.iloc[i,2] = annual_deposit
    fv_table.iloc[i,3] = (fv_table.iloc[i,1] + fv_table.iloc[i,2]) * returns
    fv_table.iloc[i,4] = (fv_table.iloc[i,1] + fv_table.iloc[i,2]) \
    * returns + annual_deposit + fv_table.iloc[i,1]

# Running the for loop for the second phase
for i in range(20,50):
    fv_table.iloc[i,1] = fv_table.iloc[(i-1),4]
    fv_table.iloc[i,3] = (fv_table.iloc[i,1] + fv_table.iloc[i,2]) * returns
    fv_table.iloc[i,4] = (fv_table.iloc[i,1] + fv_table.iloc[i,2]) \
    * returns + fv_table.iloc[i,1]
    

# Saving Table for Tom
fv_table_tom = fv_table
# ------------------------------------------------------------------------------------
# Setup variables
returns = 0.075
annual_deposit = 3600
# Create empty table
fv_table = np.zeros((21,5))
fv_table = pd.DataFrame(fv_table)
fv_table.columns = ['Year', 'beg_val', 'deposit', 'ret', 'end_val']
fv_table['Year'] = np.arange(1,22)
fv_table['Year'] = np.arange(30,51)
# Computer the first row values
fv_table.iloc[0,2] = annual_deposit
fv_table.iloc[0,3] = annual_deposit * returns
fv_table.iloc[0,4] = fv_table.iloc[0,3] + fv_table.iloc[0,2]
# Run the for loop
for i in range(1,21):
    fv_table.iloc[i,1] = fv_table.iloc[(i-1),4]
    fv_table.iloc[i,2] = annual_deposit
    fv_table.iloc[i,3] = (fv_table.iloc[i,1] + fv_table.iloc[i,2]) * returns
    fv_table.iloc[i,4] = (fv_table.iloc[i,1] + fv_table.iloc[i,2]) \
    * returns + annual_deposit + fv_table.iloc[i,1]
    
fv_table_jerry = fv_table 

# ------------------------------------------------------------------------------------
# join the tables
fv_table_both = pd.merge(fv_table_tom,fv_table_jerry, on = "Year", how = "outer")
# Rename the columns
fv_table_both.columns = ["Year", "Tom's initial value", "Tom's Deposit",\
                         "Tom's Interest", "Tom's Ending value", \
                         "Jerry's initial value", "Jerry's Deposit", \
                         "Jerry's Interest", "Jerry's Ending value"]
                         
                         
fv_table_both = fv_table_both.fillna(0).round(2)
# Showing only 3 columns 
print(fv_table_both[["Year", "Tom's Ending value", "Jerry's Ending value"]]) 


#We can also plot the savings chart for both Tom and Jerry.

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = plt.axes([0.1,0.1,0.8,0.8])
ax1.plot(fv_table_both['Year'], fv_table_both['''Tom's Ending value'''], label = "Tom's Saving")
ax1.plot(fv_table_both['Year'], fv_table_both['''Jerry's Ending value'''], label = "Jerry's Saving")
ax1.set_xlabel("Years")
ax1.set_ylabel("Saving growth")
plt.legend(loc = "best")
plt.show()
    