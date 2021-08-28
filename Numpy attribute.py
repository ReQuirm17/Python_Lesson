#ใช้เพื่อบอกโครงสร้างของ array
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.ndim) #attribute to told dimension
print(a.dtype) #attribute for data type
print(a.shape) #attribute to tell shape(member) 5row 0col
print(b.shape) #3row 3col
print(b.size) #attribute to tell howmany member in array
print(b.itemsize) #attribute to find byte of array(1byte  = 8 bit)


