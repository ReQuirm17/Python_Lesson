from tkinter import *
def leftClickbutton(event):
    print("Left Click")

def doubleClickbutton(event):
    print("Double Click")

main = Tk()
button = Button(main,text="My button")
button.pack()
button.bind('<Button-1>',leftClickbutton)
button.bind('<Double-1>',doubleClickbutton)
main.mainloop()