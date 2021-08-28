#member on diagonal=1 other=0
import numpy as np
a = np.identity(4) #identity จะบังคับในเเบบ square metrix
print(a)
print("-----------------------------")
b = np.identity(5,dtype="int")
print(b)
print("-----------------------------")
c = np.eye(3,4) #eye ยืดหยุ่นขนาดได้
print(c)
print("----------------------------")
print(np.eye(5))
print("----------------------------")
d = np.eye(5,k=1) #เคลื่อนขึ้น 1 col
e = np.eye(5,k=-1)#เคลื่อนลง 1 col
print(d)
print("----------------------------")
print(e)
print("----------------------------")