# Employee management system
from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get()=='Shubham' and passwordEntry.get()=='12345':
        messagebox.showerror('Success', 'Login is successful')
        root.destroy() 
        import ems
    else:
        messagebox.showerror('Error' , 'Wrong Credentials')

root =  CTk()
root.geometry('978x554')
root.resizable(0,0)
root.title('Login Page')
image = CTkImage(Image.open('img2.jpeg'), size=(978 , 554))

imageLabel = CTkLabel(root, image=image , text='')
imageLabel.place(x=0 , y=0)
headinglable = CTkLabel(root, text= 'Employee management system', bg_color='#FAFAFB', font=('Goudy Old Style' , 20 , 'bold'), text_color='dark blue')
headinglable.place(x=360 , y=9)

usernameEntry = CTkEntry(root,placeholder_text='Enter your Username',width=180)
usernameEntry.place(x=10 , y=15)

passwordEntry = CTkEntry(root,placeholder_text='Enter your Password',width=180 , show = "*")
passwordEntry.place(x=10 , y=50)

loginButton = CTkButton(root , text='Login' , width=100, cursor = 'hand2', command=login)
loginButton.place(x= 40 , y = 85)



root.mainloop() 


