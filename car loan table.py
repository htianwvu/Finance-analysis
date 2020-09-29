# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:19:48 2020

@author: htian
"""

''''''
#Car price $15000
#Loan amount $10000
#Interest rates 7% per year
#Duration 5 years
#Payments ? - We need to solve for this.
''''''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


car_loan = 10000
interest = 0.07
years = 5
car_payments = np.pmt(rate = interest, nper = years, pv = -car_loan)
# print(car_payments)
# This creats a table of 5 rows and 6 columns filled with zeros   
loan_table = np.zeros((5,6))

# Convert it to a dataframe
loan_table = pd.DataFrame(loan_table)
# We change the column names to relevant fields
loan_table.columns = ["Year", 'Initial_Balance', "Payments", "Interest",
                       "Principal", "Ending_Balance"]

print(loan_table)

# fill the very intital numbers
# Row 0 and column 0 is our Year 1.
# use iloc[] to loacate that
loan_table.iloc[0,0] = 1

# Initial balance it the car_loan amount
loan_table.iloc[0,1] = car_loan
# car payments are the same we calculated above
loan_table.iloc[0,2] = car_payments

# interest payment is initial balance * interest
loan_table.iloc[0,3] = car_loan * interest
loan_table.iloc[0,4] = car_payments - (car_loan * interest)

# Priciple is car payment - interest
loan_table.iloc[0,5] = car_loan - (car_payments - (car_loan * interest))
# Ending balance is intial balance - principle

# Our loop will run from row 1 to 4

for i in range(1,5):
# First row is the year
    loan_table.iloc[i,0] = i + 1
    # The initial balance is previous years ending balance
    loan_table.iloc[i,1] = loan_table.iloc[(i-1), 5]
    # The payments are the car payments
    loan_table.iloc[i,2] = car_payments
    # Interest each year is initial balance * interest rate
    loan_table.iloc[i,3] = loan_table.iloc[i,1] * interest
      # Principle amount is payment - interest amount
    loan_table.iloc[i,4] = car_payments - (loan_table.iloc[i,1] * interest)
    # Ending balance is initial balance - principle
    loan_table.iloc[i,5] = loan_table.iloc[i,1] - (car_payments - (loan_table.iloc[i,1] * interest))

# We want to round all the values to 2 places   
loan_table = loan_table.round(2)

# It is used to display the entire pandas dataframe

with pd.option_context("display.max_rows",None,"display.max_columns", None):
    print(loan_table)
    
    