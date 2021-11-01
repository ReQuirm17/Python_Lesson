import pandas as pd
data_ls = [10,21,52,64,"bt","ul"] #list(array 1d)
data_tp = (10,20,78,9452,656) #tuple
print(data_ls)
print(pd.Series(data_ls)) #make row and col from list
print('')
print('')
print(pd.Series(data_tp))
