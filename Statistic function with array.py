import numpy as np
# 1 dimension
a = np.array([12,65,989,15,465,684,79])
b = a.sum() #sum of data in array
c = a.prod() #multiplication of data in array
d = a.mean() #average of data in array
e = a.max() #Maximum data in array
f = a.min() #Minimum data in array
g = a.argmax()#to find index that have maximum data
h = a.argmin()#to find index that have minimum data
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print("-----------------------------------------------")
#2 dimension ใช้2-10 ได้หมดเเต่ต้องใส่เเกน [เเนวตั้ง(axis0),เเนวนอน(axis1)]
b = np.array([[231,654,987],[789,321,195],[537,258,582]])
print(b)
print("                                                        ")
print(np.min(b,axis=1))#Minimum data in array เเนวนอน
print("-----------------------------------------------")
print(np.min(b,axis=0))#Minimum data in array เเนวตั้ง
print("-----------------------------------------------")
print(np.max(b,axis=1))#Maximum data in array เเนวนอน
print("-----------------------------------------------")
print(np.max(b,axis=0))#Maximum data in array เเนวตั้ง
print("-----------------------------------------------")
print(np.average(b,axis=1))