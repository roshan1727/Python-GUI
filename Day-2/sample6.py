from tkinter import *

root=Tk()

root.geometry("350x550")
root.maxsize(350,550)
root.minsize(350,550)
root.title("hello sir")

label1=Label(root,text="FirstName")
label1.pack()
label2=Label(root,text="LastName")
label2.pack()

username=StringVar()
passwd=StringVar()

username=Entry(root,textvariable=username).grid(row=0,column=1)
passwd=Entry(root,textvariable=passwd).grid(row=2,column=1)

# btn1=Button(text="Click me")
# btn1.pack()



root.mainloop()