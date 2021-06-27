from tkinter import *

root=Tk()

root.geometry("655x775")

# frames are similar to div in website
frampanuro=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN,)
frampanuro.pack(side=TOP)

l=Label(frampanuro,text="GST Billling")
l.pack()

f2=Frame(root,background="blue",borderwidth=8,relief=GROOVE)
f2.pack()
label1=Label(f2,text="File panuro file panuro gst ya")
label1.pack(side=BOTTOM,fill=X)
root.mainloop()