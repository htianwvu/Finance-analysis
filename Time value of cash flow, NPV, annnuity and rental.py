import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# setting interest rat to 2%

r = 0.02
cf = pd.DataFrame({'Year':[1,2,3,4,5], "cash_flow":[100,100,100,100,100]})
cf["pv"] = cf['cash_flow'] / (1.0 + r)**cf['Year'] # present value
npv = cf["pv"].sum()
cf
npv

# plot net present value (NPV)

fig = plt.figure(figsize=(11,8))
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(cf["Year"], cf["pv"])
ax1.set_xlabel('Years') # Notice the use of set_ to begin methods
ax1.set_ylabel('PV')
ax1.set_title('Present Value Chart')
plt.show()

###Calculating net present value of uneven cash flows
cf = pd.DataFrame({"Year":[1,2,3,4,5],
                   "cf":[100,200,300,400,500]})
print(cf)

r = 0.05
cf["pv"] = cf["cf"] / (1 + r)**cf["Year"]
npv = cf["pv"].sum()
print(npv)

#Calculating the PV with negative cash flow
cf = pd.DataFrame({"Year":[0,1,2,3,4,5],
                   "cf":[-250,100,100,100,100,250]})
print(cf)

r = 0.05
cf["pv"] = cf["cf"] / (1 + r)**cf["Year"]
npv = cf["pv"].sum()
print(npv)

##Calculating the present value of a finite annuity
#Let us suppose you win a $50000 lottery and you are given two options
#Receive five equal payments of $10000
#Lump sum $45000.
#Let us suppose the bank pays 5% interest rate on the deposit.

# option 1
pmt = 10000
n = 5
r = 0.05
cf = pd.DataFrame({'period':np.arange(1,6),
                   "pmt":pmt})   # numpy form an array of 1-6
print(cf)


# option 2 intest rate = 0.05

r = 0.05
cf["pv"] = cf['pmt']/(1 + r) ** cf["period"]
npv = cf["pv"].sum()
print(npv)

#Calculating the present value infinite annuity
#buy a bond that pays $1000 per year in interest forever. 
#If the current interest rate is 5%

cf = 1000
r = 0.05
value = cf/r
print(value)

#Calculating present value of finite growing annuity, or rent 

# Suppose you own an apartment complex. The tenants pay you 
#a fixed rent every month. You can increase the rent to tackle 
#higher inflation. This apartment building may be described as 
#an annuity payment that grows at the rate of inflation. 

payment = 1000
growth = 0.03 # Growth rate of the payments
n = 5 # number of year
rate = 0.06 # Interest rates
cf = pd.DataFrame({"period":np.arange(1,6),
'cf':payment})
print(cf)
cf["cf"] = payment * (1 + growth) ** (cf["period"] - 1)
print(cf)
cf["pv"] = cf["cf"] / (1 + rate) ** cf["period"]
print(cf)

npv = cf["pv"].sum()
print("The NPV of growing payments is", + npv)


