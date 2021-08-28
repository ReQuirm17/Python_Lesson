import numpy as np
a = np.array([[1,2,3],[4,5,6]]) #array 2 d([[]]) row 0 [1,2,3,4,5] row 1 [6,7,8,9,10]
print(a, a.ndim)
print("-----------------------------------")
li = [[1,2],[3,4],[5,6],[7,8]] # 4 row as list
c = np.array(li)
print(c)
print("-----------------------------------")
tu = ((1,2),(3,4)) # 2 row as tuple
d = np.array(tu)
print(d)