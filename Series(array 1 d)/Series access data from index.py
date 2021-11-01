import pandas as pd
data = {"banana":50,"mango":100,"coconut":145} #dictionary
ps = pd.Series(data)
print(ps)
print("")

print(ps['banana']) #index banana
print(ps[1],ps[2]) #index[1] ,[2]
