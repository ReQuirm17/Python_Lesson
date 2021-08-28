#กำหนดช่วงสมาชิกได้ในขนาดเท่าๆกัน
import numpy as np
a = np.linspace(1,3) #start,stop
print(a)
print("---------------------------------------------")
print(np.linspace(1,5,4)) #start,stop,amount member
print("---------------------------------------------")
b = np.linspace(1,5,endpoint=False) #stop ก่อนถึง 5
print(b)