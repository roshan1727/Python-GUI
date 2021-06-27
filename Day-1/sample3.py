from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
#from PIL import Image,ImageT #to create a GUI window Box
Boxvariable=Tk()



Boxvariable.geometry("744x434")  #GUI window box 
typeimage=Image.open("Assets/lumosity2.jpg")
photo=ImageTk.PhotoImage(typeimage)

Labelling=Label(image=photo)
Labelling.pack()
 


# # This whole thing accept only png format 

# # assiging an image to the variable 
# photo=PhotoImage(file="Assets/img1.png")
# # the must be labed to have no user interaction
# imgaeLabel=Label(image=photo)
# # anything is labed must be packed to show in the GUI window 
# imgaeLabel.pack()


# NameLabel=Label(text="Hello boss")  #non interactive txt 
# NameLabel.pack()

Boxvariable.mainloop()  #main body
 