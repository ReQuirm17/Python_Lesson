from tkinter import * #import everything in library

def sayHelloworld():
    print("Hello world")

mainWindow = Tk() #Assign Tkinter main control !must be first widget!
button = Button(mainWindow,text = "click here",command = sayHelloworld) #ปุ่มเเสดงผลด้วย tkinter มีชื่อบนปุ่มว่า click here(attribute) เเละ มีการดำเนินการหลัง click ตามตัวเเปร sayHelloworld ภายใต้ function
button.place(x=50, y=20) #กำหนดระนาบ (x,y,z) บน tkinter
button2 = Button(mainWindow,text = "click here",command = sayHelloworld)
button2.place(x=150, y=100)
mainWindow.mainloop()