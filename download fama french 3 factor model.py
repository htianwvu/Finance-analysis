# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:35:55 2020

@author: htian
"""
import urllib.request
import zipfile
ff_url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip"
# Download the file and save it
# We will name it fama_french.zip file
urllib.request.urlretrieve(ff_url,'fama_french.zip')
zip_file = zipfile.ZipFile('fama_french.zip', 'r')
# Next we extact the file data
# We will call it ff_factors.csv
zip_file.extractall()
# Make sure you close the file after extraction
zip_file.close()
import pandas as pd
ff_factors = pd.read_csv('F-F_Research_Data_Factors.csv', skiprows = 3)
print(ff_factors.head())

print(ff_factors.tail())

#So the unwanted data is still in our dataframe. 
#Lets confirm the rows are indeed 1114 on wards.

print(ff_factors.iloc[1112:1120],)


# select the first 1114 rows use nrow()

ff_factors = pd.read_csv('F-F_Research_Data_Factors.csv', skiprows = 3,
nrows = 1114)
print(ff_factors.tail())


# select the first row as our index

ff_factors = pd.read_csv('F-F_Research_Data_Factors.csv', skiprows = 3,
nrows = 1114, index_col = 0)
print(ff_factors.tail())

#we will convert our index into a date object.

ff_factors.index = pd.to_datetime(ff_factors.index, format= '%Y%m')
print(ff_factors.tail())

# change to end of month using the pd.offset method.

ff_factors.index = ff_factors.index + pd.offsets.MonthEnd()
print(ff_factors.tail())


##convert the numbers into decimals. We will use a simple lambda function to that.

ff_factors = ff_factors.apply(lambda x: x/ 100)
ff_factors.tail()



