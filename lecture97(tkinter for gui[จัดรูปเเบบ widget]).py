from tkinter import *

main = Tk()

text1 = Label(main, text="Hello World", width=20, fg="red", bg="yellow", font=("Helvetica", 76), anchor=W).grid(row=0,
                                                                                                         column=1)
text2 = Label(main, text="Hello World", width=20, fg="red", bg="yellow", font=("Helvetica", 76), anchor=E).grid(row=1,
                                                                                                         column=2)
main.mainloop()
