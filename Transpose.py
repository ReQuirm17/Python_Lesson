#change rol to col chnge col to row
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3,4,5],[6,7,8,9,10]])
a = x.transpose()
b = y.transpose()
print(x)
print(a)
print("--------------------")
print(y)
print(b)