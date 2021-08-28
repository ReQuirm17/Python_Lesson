#chane n d to 1 d
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print(a)
print("-----------------------------")
print(a.flatten()) #change 2 d to 1 d ชั่วคราว
print(a)
print("-----------------------------")
x = a.flatten()
print(x)
x[0] = 5
x[1] = 10
print(x)
print("-----------------------------")
c = a.ravel() #change data and dimension เเบบถาวร
c[0] = 5
c[1] = 10
print(c)
print(a)
