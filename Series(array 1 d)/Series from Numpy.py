import pandas as pd
import numpy as np
data_ls = [10,82,'oett','420.55','rice']#list
ndata = np.array(data_ls)
ps = pd.Series(ndata)
print(ps)