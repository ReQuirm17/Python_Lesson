#split data in array in to group that have same member กลุ่มละเท่าๆกัน
import numpy as np
#1d
a = np.arange(1,21)
print(a)
print(np.split(a,4)) #split(array,group)
print(np.split(a,10))
print(np.split(a,20))
print("====================================")
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
print(b)
print("                                                             ")
c = np.hsplit(b,4) #hsplit(array,group) จัดกลุ่มใหม่ในเเนวตั้ง
d = np.vsplit(b,5) #vsplit(array,group) จัดกลุ่มใหม่ในเเนวนอน
print(c)
print("                                                            ")
print(d)
