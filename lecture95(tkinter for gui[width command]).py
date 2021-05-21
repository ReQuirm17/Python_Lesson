from tkinter import * #import everything in library

def sayHelloworld():
    print("Hello world")

mainWindow = Tk() #Assign Tkinter main control !must be first widget!
button = Button(mainWindow,text = "click here1",command = sayHelloworld,width=20,height=10).grid(row=2,column=1)
button2 = Button(mainWindow,text = "click here2",command = sayHelloworld).grid(row=1,column=1)
button3 = Button(mainWindow,text = "click here3",command = sayHelloworld).grid(row=0,column=2)
label = Label(mainWindow, text = "Hello", width=20).grid(row=0, column=1)
mainWindow.mainloop()