#การเข้าถึงสมาชิกตามช่วงที่กำหนด
#index+1 = target member
import numpy as np
a=np.arange(1,11)
print(a)
print(a[:]) #get every data in array
print(a[5:]) #start(เป็นต้นไป)
print(a[:5])#เอาสมาชิกจนถึง index ที่5

b = np.array([20,18,65,23,144])
print(b)
print(b[1:])
print(b[2:4]) #เข้าถึงสมาชิกตั้งเเต่ indexที่ 2 ก่อนถึง index ที่ 4

print(a[2:9:2]) #start:stop:step(กระโดดข้ามสมาชิก)
print(b[0:3:2])

c = np.arange(10,20)
print(c)
print(c[::2])

