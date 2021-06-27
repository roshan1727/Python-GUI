from tkinter import *

window=Tk()

Canva_widht=800
canvas_height=800

window.title("GST Filling")
window.geometry(f"{Canva_widht}x{canvas_height}")
canwidget=Canvas(window,width=Canva_widht,height=canvas_height).pack()
# window.maxsize(550,550)
# window.minsize(550,550)

Label(window,text="GST FILLING APP",font="arial 24",background="grey").grid(row=0,column=3)
l1=Label(window,text="Name of Product",padx=4,pady=4).grid(row=3,column=2)
l2=Label(window,text="Quantity",padx=4,pady=4).grid(row=4,column=2)
l3=Label(window,text="Rate",padx=4,pady=4).grid(row=5,column=2)
l4=Label(window,text="GST",padx=4,pady=4).grid(row=6,column=2)

Product=StringVar()
quantity=StringVar()
rate=StringVar()
gst=StringVar()


Product=Entry(window,textvariable=Product).grid(row=3,column=3)
quantity=Entry(window,textvariable=quantity).grid(row=4,column=3)
rate=Entry(window,textvariable=rate).grid(row=5,column=3)
gst=Entry(window,textvariable=gst).grid(row=6,column=3)

Button(text="Add Panuga Baaa",foreground="white",background="black",padx=4,pady=5).grid(row=7,column=3)








window.mainloop()