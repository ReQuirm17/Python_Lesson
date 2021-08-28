#reshape--->change dimension(ชั่วคราว(เปลี่ยนเเค่ตอนเรียกมิติเดิมคงอยู่)
#resize--->change dimension ถาวร
import numpy as np
a = np.arange(10) #1d
print(a)
x = a.reshape(2,5)#reshape(row,col)
print(x)
print("------------------------------------")
print(a)
print("------------------------------------")
y = a.resize(2,5) #resize(row,col)
print("-------------------------------------")
print(a)


