import pandas as pd
import numpy as np
items = ['rice','mango','banana'] #list
idx = [10,20,30]
ps = pd.Series(items,index=idx) #pd.Series(list,index_set)
print(ps)