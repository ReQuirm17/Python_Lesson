import numpy as np

arr = np.array(1)   #array 0 d
arr = np.array(2)
arr.ndim            #attribute for check array dimension
print(arr, arr.ndim)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #array 1 d
print(a, a.ndim)

to = [10, 20, 30, 40]
b = np.array(to)
print(b, b.ndim)

li = (5, 4, 3, 2) #touple data type
c = np.array(li)
print(c, c.ndim)
