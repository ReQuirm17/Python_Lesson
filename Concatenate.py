#Merge array
import numpy as np
a = np.array([3,4,5,9])
b = np.array([7,10,8,3])
c = np.concatenate((a,b)) #Merge between 2 array(column เพิ่ม)
d = np.append(b,77)
e = np.append(b,np.arange(10))
print(c)
print("------------------------------------")
print(np.append(a, 100)) #(array,new data)
print(a)
print("------------------------------------")
print(d)
print("------------------------------------")
print(e)
print("------------------------------------")
#2d
b = np.array([[1,2],[3,4]])
h = np.append(b,[[10],[20]],axis=1) #เอา 10 20 ไปต่อท้ายในเเนวนอนของเเต่ละ row
print(h)
