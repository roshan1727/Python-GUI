from tkinter import *


# event is used to handle the thinngs happen
def hack(event):
    print(f"Yoou have click me {event.x},{event.y}")

window=Tk()
window.title("GST Billing System")

width_canva=750
height_canva=600

window.geometry(f"{width_canva}x{height_canva}")

widget=Button(window,text="Help me")
widget.pack()

# bind is used to do action nd show the impact,<buttion-1> gives the info about mouse action
widget.bind('<Button-1>',hack)

# Double-1 (clicking the button twice a action trigre) and quit is used to quit when the event is held
widget.bind('<Double-1>',quit)


window.mainloop()