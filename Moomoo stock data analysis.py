# Section0 开场
##print("-"*30 + "Begin Section 0 开场" + "-"*30)
##print("这是Python的第八次课程,主要讲数据操作:")
##print("1.数值替换\n2.数值排序\n3.数值排名")
##print("-"*30 + "End Section 0 开场" + "-"*30)
##print('\n')


import pandas as pd
import numpy as np
import yfinance as yf

## import all data from moomoo
csv_file_path = 'C:/Users/htian/Desktop/swing trading/20200927072224.csv'

allstock = pd.read_csv(csv_file_path)

print(allstock,"\n")
print(allstock.info(),'n')

# delete 'Bid Price','Ask Price','Bid Vol','Ask Vol','Industry'

allstock1 = allstock.drop(['Bid Price','Ask Price','Bid Vol','Ask Vol','Industry'],axis=1)
print(allstock1.info(),'n')

## delete nan#

allstock2= allstock1.dropna(axis=0,how='all')
allstock2= allstock2.dropna(axis=1,how='all')

print(allstock2.info(),'n')

# Price 由大到小排列“
print(allstock2.sort_values(by = ["Price"],ascending = False))

## 删去最新价》300 或10 的股票

#outfile = df1[(df1[u'设计井别']=='11') & (df1[u'投产井别']=='11') &(df1[u'目前井别']=='11')]

allstock3 = allstock2[(allstock2[u"Price"] <= 300) &(allstock2[u"Price"] >=10)] 
print(allstock3.head())
print(allstock3.sort_values(by = ["Price"],ascending = False))
print(allstock3.info(),'n')
allstock3.to_csv('allstock31.txt',header=None, index=None, sep=' ', mode='a')


## 60日涨跌幅<0

txt_file_path = 'C:/Users/htian/Desktop/swing trading/allstock31.txt'

allstock4 = pd.read_table(txt_file_path, delim_whitespace=True)
print(allstock4.info(),'n')
print(allstock4,"\n")


allstock4["60d Ranking"] = pd.to_numeric(allstock4["60d Ranking"], errors="coerce").fillna(0)
print(allstock4.info(),'n')

Print('XXXX')


allstock5 = allstock4[(allstock4[u"60d Ranking"] <0)] 
print(allstock5.info(),'n')


#df['one'] = df['one'].map(convert_to_int_with_error)
#df = df.convert_objects(convert_numeric=True)


#60d Ranking


allstock3.to_excel('allstock39.xls')




allstock3 = np.array(allstock3,dtype = float)
print(allstock3.info(),'n')




allstock3["60d Ranking"] = pd.to_numeric(allstock3['60d Ranking'])




print(allstock3.sort_values(by = ["60d Ranking"],ascending = False))


allstock3["60d Ranking"] = pd.to_numeric(allstock3['60d Ranking'],errors="ignore")
print(allstock3.head())
print(allstock3.info(),'n')
print(allstock3.sort_values(by = ["60d Ranking"],ascending = False))
print(allstock3.head())





allstock4 = allstock3[(allstock3.60d Ranking] > 0)]
print(allstock4.head())



allstock3.to_excel('allstock37.xls')

allstock3.to_excel('allstock38.xls')


#allstock4 = allstock3[(allstock3.60d Ranking] > 0)]
#print(allstock4.head())



#print(allstock2.sort_values(by = ["60日涨跌幅"],ascending = False))


#allstock3.to_excel('allstock3.xls')












# Section1 数值替换
# 一对一替换
# 将顶踩比例 200.00% 替换成 100.00%
# 一定要重新赋值给顶踩比例
print("将顶踩比例 200.00% 替换成 100.00%")
df['顶踩比例'] = df['顶踩比例'].replace(2.000,1.000)
print(df,'\n')

df = df1
# 也可以将所有2.000 替换成 1.000
print("将所有的 2.000 替换成 1.000")
df = df.replace(2.000,1.000)
print(df,'\n')

# 多对一替换
df = df1
# 将 480 和 342 的替换成 1314
print("多对一替换：")
df = df.replace([480,342],1314)
print(df,'\n')

# 多对多替换
df = df1
print("多对多替换：")
df = df.replace({480:400,342:300})
print(df,'\n')


df = df1

# Section2 数值排序

# 按照观看次数升序排列
print("按照观看次数升序排列：")
print(df.sort_values(by = ["观看次数"],ascending = True))

print("按照观看次数降序排列：")
print(df.sort_values(by = ["观看次数"],ascending = False))

# 将第二行的发布时间设为None
df.loc[[1],["发布时间"]] = None
print("将第二行的发布时间设为None：")
print(df)

# 按照发布时间从晚到早拍，空值排在最开始
print("按照发布时间从晚到早拍，空值排在最开始：")
print(df.sort_values(by = ["发布时间"],ascending = False,na_position = "first"))

print("按照发布时间从早到晚拍，空值排在最后：")
print(df.sort_values(by = ["发布时间"],na_position = "last"))


# 按照多列排序
# 按照顶踩比例降序，观看次数升序排列
print("按照顶踩比例降序，观看次数升序排列：")
print(df.sort_values(by = ["顶踩比例","观看次数"],ascending = [False,True]))

# Section3 数值排名
# 用rank(ascending,method)函数进行排名
# ascending表明是升序还是降序，method有average、first、min、max 这4种取值
# 按照顶踩比例，降序排列
print("顶踩比例：")
print(df["顶踩比例"])
# average
print(df["顶踩比例"].rank(ascending = False,method = "average"))

# first
print(df["顶踩比例"].rank(ascending = False,method = "first"))

# min
print(df["顶踩比例"].rank(ascending = False,method = "min"))

# max
print(df["顶踩比例"].rank(ascending = False,method = "max"))




