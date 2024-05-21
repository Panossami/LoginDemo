import os
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


signwin=Tk()
signwin.title("SignUp")
signwin.geometry("700x400")
signwin.resizable(0,0)

check=0
def show():
    global check
    if check==0:
        passB.configure(text="◉")
        passentry.configure(show="")
        check=1
    else:
        passB.configure(text="◡")
        passentry.configure(show="*")
        check=0

def signed():
    if usentry.get()=="" or passentry.get()=="" or nameentry.get()=="":
        messagebox.showwarning("Failed","Name,Username and Password fields can't be empty")
    else:
        messagebox.showinfo("Success","Signed Up")
        signwin.destroy()
        os.system("Login.py")

def already():
    signwin.destroy()
    os.system("Login.py")


bgImage=ImageTk.PhotoImage(file="bg.jpg")
mastercanvas=Canvas(signwin,width=700,height=400,highlightthickness=0)
mastercanvas.pack()
mastercanvas.create_image(0,0,image=bgImage,anchor="nw")

mastercanvas.create_text(350,50,text="Sign Up",font="Arial 20 bold",fill="white")
#name
mastercanvas.create_text(200,150,text="Name: ",font="Arial 13",fill="white")
nameentry=Entry(signwin,width=20,font="Arial 13")
nameentry.place(x=260,y=140)

#username
mastercanvas.create_text(200,190,text="Username: ",font="Arial 13",fill="white")
usentry=Entry(signwin,width=20,font="Arial 13")
usentry.place(x=260,y=180)

#password
mastercanvas.create_text(200,230,text="Password: ",font="Arial 13",fill="white")
passentry=Entry(signwin,width=20,font="Arial 13",show="*")
passentry.place(x=260,y=220)
passB=Button(signwin,text="◡",command=show)
passB.place(x=450,y=220)

accB=Button(signwin,text="Already have an Account?",command=already)
accB.place(x=150,y=280)

signB=Button(signwin,text="Sign Up",width=12,command=signed)
signB.place(x=350,y=280)



signwin.mainloop()