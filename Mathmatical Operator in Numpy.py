import numpy as np
a = np.array([1,2,3,4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)
print(a%2)
print("---------------------")
b = np.arange(1,5)
print(b)
print(a+b) #array + array must be same dimension
print(a-b)
print(a*b)
print("---------------------")
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,8,9],[10,11,12]])
print(x)
print(y)
print("                              ")
print(x+y)
print("---------------------")
print(x-y)
print("---------------------")
print(x**y)
print("---------------------")
print(x/y)
print("---------------------")
print((x+2-y+3)*10)
print("---------------------")
z = np.array([1,5,7])
print(x)
print(z)
print("                                 ")
print(x+z) #addition in term boardcast(addition every row in x(2d) by z(1d))
print("===================================================")
print("Boardcast")
i = np.array([[1,2],[3,4],[5,6]])
j = np.array([2])
m = np.array([10,20])
print(i)
print(j)
print(m)
print("                                 ")
print(i+j)
print("--------------------------------------------")
print(i+m)

