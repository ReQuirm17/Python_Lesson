import pandas as pd
data = ([10,20,30,40,50,60,70,80,90,100])
ps = pd.Series(data)
print(ps)
print(ps[:]) #every index
print("")
print(ps[0:4]) #index 0-3
print("")
print(ps[1:]) #index 1 above
print("")
print(ps[:3]) #until index2