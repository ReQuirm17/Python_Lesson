import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
#x[row(start{ตั้งเเต่...}:stop{ก่อนถึง...}),col(start{ตั้งเเต่...}:stop{ก่อนถึง...})]
#x[row(start:stop:step),col(start:stop:step)

print(x)
print("------------------------------")
print(x[1:, 1:])#row 1 onwards  col 1 onwards
print("------------------------------")
print(x[2:, 2:])
print("------------------------------")
print(x[2: ,1:])
print("------------------------------")
print(x[:,2:])
print("------------------------------")
print(x[1:, 0:])
print("------------------------------")
print(x[:2,:])#row1 onwards col every col
print("------------------------------")
print(x[:2,2:])
print("------------------------------")
print(x[1:2,1:2])#row1stop
print("------------------------------")
print(x[2:3,0:1])
print("------------------------------")
print(x[1:3,0:3])
print("------------------------------")
print(x[::2,:]) #row 0-2,step 2(jump over row)
print("------------------------------")
print(x[1:2,:])
print("------------------------------")
print(x[::,::2])

