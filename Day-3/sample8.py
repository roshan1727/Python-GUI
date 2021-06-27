from tkinter import *

    

window=Tk()

def getvales():
    print("It works")



window.geometry("500x500")
window.maxsize(500,500)
window.minsize(500,500)

# heading for our software
heading=Label(window,text="GST Billing System",font="comicsansms 20 bold",padx=10,pady=10).grid(row=0,column=3)

# text for the system and packed it using gird
Firstname=Label(window,text="FirstName").grid(row=1,column=2)
LastName=Label(window,text="LastName").grid(row=2,column=2)
PhoneNumber=Label(window,text="PhoneNumber").grid(row=3,column=2)

# declaring to get values 
FirstnameValue=StringVar()
LastNameValue=StringVar()
PhoneNumberValue=StringVar()
Companyuser=IntVar()

# entry box for each text,packed using grid
FirstnameValue=Entry(window,textvariable="FirstNameValue").grid(row=1,column=3)
LastNameValue=Entry(window,textvariable="LastNAmeValue").grid(row=2,column=3)
PhoneNumberValue=Entry(window,textvariable="PhoneNumer").grid(row=3,column=3)


# checkbox
Companyuser=Checkbutton(text="New USer",variable=Companyuser).grid(row=6,column=3)

Button(text="Submit",command=getvales).grid(row=7,column=3)



window.mainloop()

