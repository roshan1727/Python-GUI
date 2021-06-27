from tkinter import *

window=Tk()

Canva_widht=800
canvas_height=800

window.title("GST Filling")
window.geometry(f"{Canva_widht}x{canvas_height}")
canwidget=Canvas(window, width=Canva_widht, height=canvas_height)
canwidget.pack()

# To create a rectaangeel inside GUI 
# To give coord top left and to give coord bottom right 
# canwidget.create_rectangle(0,0,700,300,fill="grey")
canwidget.create_text(200,200,text="hfvhvgi",fill="red")

canwidget.create_oval(344,233,244,233,fill="blue")



window.mainloop()