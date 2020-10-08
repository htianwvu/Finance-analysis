
# get the historical asset class returns


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# load our url
my_url = urlopen('https://www.portfoliovisualizer.com/historical-asset-class-returns')
# Read the url into BeautifulSoup
soup = BeautifulSoup(my_url.read(), 'lxml')

# saves all the column names.

# Select just the column names
col_names = soup.tr
# Split Column names
col_names = col_names.text.split('\n')
# Delete any empty or None values
col_names = list(filter(None,col_names))

# get all the returns data and save it as a list

data = []
for t in soup.find_all('td'):
    data.append(t.text)
    
#The data list contains unwanted entry located at the very end. So we will delete it.
del data[-1]

# Create data frame from 
df_returns = pd.DataFrame(np.array(data).reshape(49,40), columns=col_names)
# Set Year column as the index
df_returns.set_index('Year', inplace=True)
# print the first few rows
print(df_returns.head())