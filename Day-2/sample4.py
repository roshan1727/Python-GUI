from tkinter import *

#to create a GUI window
root=Tk()
root.geometry("450x455") #to give a starting size of the window
#To give the title of the GUI
root.title("My First GUI")


# # Label options
# text-add the Text
# bd-background
# fg-foreground
# font-set the Font 
# padx= x padding,ypady=y padding
# # relif=borer style=SUNKEN,RAISED,GROOVE,RIDGE
title_label=Label(text='''hello boies lets start upskilling''',background='blue',foreground='red',padx=23,pady=55,font=("Times New Roman",24,"bold"),borderwidth=3,relief=RAISED)


# Pack options:
# ANCHOR for the location
# Fill,paddx,paddy
title_label.pack(side=LEFT ,fill=Y)



root.mainloop()
