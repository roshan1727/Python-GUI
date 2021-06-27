from  tkinter import *

root=Tk()
root.geometry("750x650")

def hello():
    print("Vanakm da mapala")

frame=Frame(root,borderwidth=10,bg="blue")
frame.pack(side=LEFT,anchor='nw',padx=12)

# to create button in the GUI window 
b1=Button(frame,fg="blue",text="Fill Panura",command=hello)
b1.pack()
second_frame=Frame(root,borderwidth=10,bg="hot pink")
second_frame.pack(side=BOTTOM,anchor='nw',padx=10)

b2=Button(second_frame,fg="blue",text="Fill Panu di naye")
b2.pack()



root.mainloop()