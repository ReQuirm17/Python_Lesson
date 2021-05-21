#UpdateData ไม่ได้
tuple = (1, 3, 5, 7, 9)
print(tuple)
tuple2 = (2, 4, 6, 8, 10)
tuple3 = tuple+tuple2
print(tuple3)
print(tuple3[1])
print(tuple3[0])
print(tuple3[0:7])
tuple4 =tuple+tuple2*2
print(tuple4)
print(2 in tuple2)
print(1 in tuple2)
for i in tuple3:
    print("count",i)