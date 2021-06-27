from tkinter import *

dialogboox=Tk()  #just aGUI window

#width and height of the GUI window  box
dialogboox.geometry("733x434")

#width,height to lock the dialogbox with specific minimum box sixe
dialogboox.minsize(300,400)
#width,height to lock the dialogbox with specific maximum box sixe
dialogboox.maxsize(1000,600)

# to add txt or any type of stuff inside the GUI window and that variable to be pack
# these content cont be interact with users
LabelName=Label(text="Hello ppl this my new learning stuff using python tkinter\n myself rose")

#pack function  is used to say that GUI window has a LabelName 
LabelName.pack()

dialogboox.mainloop()