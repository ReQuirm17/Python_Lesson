from tkinter import *
import math

def leftClickbutton(event):
    print(float(textboxweight.get())/math.pow(float(textboxHight.get())/100,2))
    labelResult.configure(text=float(textboxweight.get())/math.pow(float(textboxHight.get())/100,2))
    call()

def call():
    call = float(textboxweight.get()) / math.pow(float(textboxHight.get()) / 100, 2)

    if call >= 30.00:
        print("อยู่ในเกณฑ์ภาวะอ้วนมาก")
    elif 29.9 >= call >=25.0:
        print('อยู่ในเกณฑ์ภาวะอ้วน')
    elif 23.0 >= call >= 24.9:
        print('อยู่ในเกณฑ์น้ำหนักเกิน')
    elif 18.6 >= call >= 22.9:
        print('อยู่ในเกณฑ์น้ำหนักปกติ')
    elif call <= 18.5:
        print('อยู่ในเกณฑ์ผอมเกินไป')
    labelResult.configure(text=call)

MainWindow = Tk()
labelHight = Label(MainWindow,text='ส่วนสูง(cm.)')
labelHight.grid(row=0,column=0)

textboxHight = Entry(MainWindow)
textboxHight.grid(row=0,column=1)

labelweight = Label(MainWindow,text='น้ำหนัก(kg.)')
labelweight.grid(row=1,column=0)

textboxweight = Entry(MainWindow)
textboxweight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text='คำนวณ')
calculateButton.bind('<Button-1>',leftClickbutton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text='BMI is')
labelResult.grid(row=2,column=1)

labelcall = Label(MainWindow,text='call')
labelcall.grid(row=2,column=2)


MainWindow.mainloop()