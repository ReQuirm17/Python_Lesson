#array[index,index]
import numpy as np
x = np.arange(1,10)
dex = np.array([0,5,7]) #index 0 5 7
print(x)
print(x[dex]) #compare position index x  by assign in array dex
print("------------------------------------------------------------")
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print("------------------------------------------------------------")
print(b[[0,2]]) #row(index0,2)
print("------------------------------------------------------------")
print(b[[0,2],[2,0]])#row(index0,2) col(index2,0)
print("------------------------------------------------------------")
y=np.array([3,4,5])
print(x[y])
print("------------------------------------------------------------")
m=x[[1,4,1,4,1,4,1,4]]#compare position index x  by assign in array m
print(m)
print("------------------------------------------------------------")
q = np.array([[1,-2,-3],[4,-5,9]])
print(q)
print("------------------------------------------------------------")
print(q[q<0]) #show member < 0
print(q[q>0]**2) #show member > 0 and power it with 2