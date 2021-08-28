#การเข้าถึงข้อมูลสมาชิกโดยอ้างอิงจากตำเเหน่ง(index)
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a[3]) #column ที่ 3 ในชุด Array a เก็บข้อมูล เลข 4 ไว้่
print(a[4]) #column ที่ 4 ในชุด Array a เก็บข้อมูล เลข 5 ไว้่
print(a[2]+a[0])
print(a[0]-a[4])
print(a[-1]) # a[-1] = a[4] วนถอยหลัง
a[0] = 10 #เปลี่ยนค่าใน index ที ่0
a[2] = 7 #เปลี่ยนค่าใน index ที่ 2
print(a)
print("----------------------------------------------------")
b = np.array([213,8794,6514,456,132,8231])
print(b[-2])
print(b[2])
print(b[4])