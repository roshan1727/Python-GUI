from tkinter import * 
from PIL import Image,ImageTk

window=Tk()
# title for the window
window.title("RaRo's News")
# size for the window
window.geometry("1000x1000")

texts=[]
photos=[]
for i in range(0,3):
    with open(f"C:\GitFiles\Python-GUI\Day-3\{i+1}.txt") as f:
        text=f.read()
        texts.append(text)

    image=Image.open(f"C:\GitFiles\Python-GUI\Day-3\{i+1}.png")
    #TODO:to resize the immage
    image=image.resize((155,155),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))


f0=Frame(window,width=800,height=70,padx=10,pady=10)
Label(f0,text="RaRo's News",font="lucida 33 bold").pack()
f0.pack()
Label(f0,text="June 27 2021",font="lucida 13 bold").pack()
f0.pack()

f1=Frame(window,width=900,height=200,padx=10,pady=10)
Label(f1,text=texts[0],padx=10,pady=10).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")
f2=Frame(window,width=900,height=200,padx=10,pady=10)
Label(f2,text=texts[1],padx=10,pady=10).pack(side="right")
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")
f3=Frame(window,width=900,height=200,padx=10,pady=10)
Label(f3,text=texts[2],padx=10,pady=10).pack(side="left")
Label(f3,image=photos[2],anchor="e").pack()
f3.pack(anchor="w")

# f2=Frame(window,width=)


window.mainloop()