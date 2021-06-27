from tkinter import *
from PIL import Image,ImageTk


def getvariable():
    print(Firstname.get())
    print(Lastname.get())

window=Tk()
window.geometry("400x500")
window.title("Vanakm da")

a=Label(window,text="FirstName")
b=Label(window,text="lastName")
a.grid(row=0,column=1)
b.grid(row=1,column=1)
# entry tag is simmilar to input tag in website
# # variable types BooleanVar,StringVar,DoubleVar,IntVar
Firstname=StringVar()
Lastname=StringVar()
Firstname=Entry(window,textvariable=Firstname).grid(row=0,column=2)
Lastname=Entry(window,textvariable=Lastname).grid(row=1,column=2)



Button(text="Submit",command=getvariable).grid()

# l1=label(window,text="hello").pack()



window.mainloop()