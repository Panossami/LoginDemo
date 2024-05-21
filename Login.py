from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os

loginwin=Tk()
loginwin.title("Login")
loginwin.geometry("700x400")
loginwin.resizable(0,0)

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

def createacc():
    loginwin.destroy()
    os.system("SignUp.py")


def logged():
    if usentry.get()=="" or passentry.get()=="":
        messagebox.showwarning("Failed","Username and Password fields can't be empty")
    else:
        messagebox.showinfo("Success","Logged in")
        loginwin.destroy()

bgImage=ImageTk.PhotoImage(file="bg.jpg")
mastercanvas=Canvas(loginwin,width=700,height=400,highlightthickness=0)
mastercanvas.pack()
mastercanvas.create_image(0,0,image=bgImage,anchor="nw")

mastercanvas.create_text(350,50,text="Login",font="Arial 20 bold",fill="white")

mastercanvas.create_text(200,150,text="Username: ",font="Arial 13",fill="white")
usentry=Entry(loginwin,width=20,font="Arial 13")
usentry.place(x=260,y=140)


mastercanvas.create_text(200,220,text="Password: ",font="Arial 13",fill="white")
passentry=Entry(loginwin,width=20,font="Arial 13",show="*")
passentry.place(x=260,y=210)
passB=Button(loginwin,text="◡",command=show)
passB.place(x=450,y=210)

craccB=Button(loginwin,text="Don't have an account?",command=createacc)
craccB.place(x=150,y=280)

logB=Button(loginwin,text="Login",width=12,command=logged)
logB.place(x=350,y=280)



loginwin.mainloop()