#การเข้าถึงข้อมูลสมาชิกโดยอ้างอิงจากตำเเหน่ง(index) 2 ค่า คิอ row,column [row-นอน col-ตั้ง]
import numpy as np
a = np.array([[1,2],[3,4],[5,6]]) #row0=[1,2] row1=[3,4] row2=[5,6]
print(a)
#array[row][column]
print(a[1][1]) #row1col1
print(a[2][0]) #row2col0
print(a[0][0]) #row0col0
print(a[0][1]) #row0col1
print("----------------------------------------------------")
a[0][0] = 100
a[0][1] = 200
a[1][0] = 300
print(a)
print("----------------------------------------------------")
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0][1])
print(b[2][1])
print(b[-1][-2]) #index - = down to up row0=row-3,row1=-2,row2=-3 col is same