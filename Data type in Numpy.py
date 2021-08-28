import numpy as np
#int
a = np.array([1, 2, 3, 4, 5])
print(a.dtype)
a = np.array([1, 2, 3, 4, 5], dtype="int")
print(a)
print("-----------------------------------")
#float
b = np.array([1,2,3,4,5],dtype="float")
print(b)
print("-----------------------------------")
#complex
c = np.array([1,2,3,4,5],dtype="complex")
print(c)
print("-----------------------------------")
#array 2 d
d = np.array([[1,2,3],[4,5,6]],dtype=float)
print(d)
