import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox    
import subprocess as sp
from tkinter.ttk import Combobox
import random
import pyperclip


# create the main window
m=tk.Tk()
m.title("PASSWORD GENERATOR")
m.geometry("600x600")


#======================  PAGE - 1 [Login]  =======================#

def login():
    m.Mframe = LabelFrame(m, width=600, height=600, font=('arial', 15, 'bold'), bg="light green", bd=15, relief='ridge')
    m.Mframe.grid(row=0, column=0, padx=2, pady=2)

    #----------------  Label  --------------------# 
    l1 = Label(m, text="Login", font=('Copperplate Gothic Bold', 40, "bold"))
    l1.place(x=230, y=80)
    l2 = Label(m, text="Username:", font=('Times New Roman', 17, 'bold'))
    l2.place(x=140, y=180)
    l3 = Label(m, text="Password:", font=('Times New Roman', 17, 'bold'))
    l3.place(x=140, y=240)

    #---------------- Entry box  -----------------#
    e1 = StringVar()
    e2 = StringVar()
    e1_entry = Entry(m, width=23, textvariable=e1)
    e1_entry.place(x=280, y=186)
    e2_entry = Entry(m, width=23, textvariable=e2)
    e2_entry.place(x=280, y=240)

    #--------------------  Buttons  ---------------#
    def login_clicked():
        username = e1.get()
        password = e2.get()
        if username == "santhosh" and password == "1234":  
            # Handle successful login
            messagebox.showinfo("Login","Succesfull to Login")
        else:
            # Handle unsuccessful login
            username != e1 and password !=e2
            messagebox.showwarning("Login","Sorry..! Try Again")      
            

    bt1 = Button(m, text="Continue", font=('Times New Roman', 15, "bold"), width=10, bg='green', fg='white', command=login_clicked)
    bt1.place(x=400, y=420)
    bt2 = Button(m, text="Back", font=('Times New Roman', 15, "bold"), width=10, height=1, command=open, fg="white", bg='red')
    bt2.place(x=100, y=420)
    bt3 = Button(m, text="Conform", font=('Times New Roman', 15, "bold"), width=10, height=1,command=login_clicked, fg="black", bg='white')
    bt3.place(x=250, y=330)

#===========================  PAGE - 2  ========================#

def sign():
    b1=Frame(m,width=600,height=600,bg='blue')
    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    f1=Frame(m,width=600,height=600,bg="gray")
    
    #======= LABEL ======#
    
    l1=Label(m,text="SIGNUP",font=('Illuma Black',40,"bold"))
    l1.place(x=200,y=60)
    l2=Label(m,text="Username:",font=('Times New Roman',18,'bold'))
    l2.place(x=50,y=150)
    l3=Label(m,text="Password:",font=('Times New Roman',18,'bold'))
    l3.place(x=53,y=200)
    l4=Label(m,text="Age:",font=('Times New Roman',18,'bold'))
    l4.place(x=110,y=250)
    l5=Label(m,text="Gender:",font=('Times New Roman',18,'bold'))
    l5.place(x=70,y=300)
    l6=Label(m,text="Password Generator:",font=('Times New Roman',18,'bold'))
    l6.place(x=40,y=350)
    l7=Label(m,text="Confirm Password:",font=('Times New Roman',18,'bold'))
    l7.place(x=40,y=400)

    #======== Radio Button =======#
    var=IntVar()
    Radiobutton(m,text="MALE",variable=var,value=1).place(x=190,y=300)
    Radiobutton(m,text="FEMALE",variable=var,value=2).place(x=280,y=300)
    Radiobutton(m,text="OTHERS",variable=var,value=3).place(x=380,y=300)

        #======= Buttons =========#
    bt=Button(m,text="continue",font=('Illuma Black',20,"bold"),width=10,bg='green',fg='white')
    bt.place(x=330,y=490)
    bt=Button(m,text="Back",font=('Illuma Black',20,"bold"),width=10,command=open,bg='red',fg='white')
    bt.place(x=100,y=490)
    bt=Button(m,text="Password Generator",font=('Illuma Black',15,"bold"),width=15,bg='lightblue',fg='Black',command=pass_word)
    bt.place(x=300,y=350)

       
    
    #========  Entry Box  =========#


name_entry = tk.Entry(root, fg='gray')
name_entry.insert(0, "Enter your name")
name_entry.pack()

# Change the color and font of the shadow text
def clear_entry(event):
    if name_entry.get() == "Enter your name":
        name_entry.delete(0, "end")
        name_entry.config(fg='black')

def reset_entry(event):
    if name_entry.get() == "":
        name_entry.insert(0, "Enter your name")
        name_entry.config(fg='gray')

name_entry.bind("<FocusIn>", clear_entry)
name_entry.bind("<FocusOut>", reset_entry)

    
    e1=Entry(m,width=30)
    e1.place(x=190,y=150)
    e1.insert(0,"Enter The User Name...")
    e1.bind("<FocusIn>",sign)
        
        
    e2=Entry(m,width=30)
    e2.place(x=190,y=200)
    e2.insert(0,"Enter The Password...")
    e2.bind("<FocusIn>",sign)

    e3=Entry(m,width=25)
    e3.place(x=300,y=400)
    e3.insert(0,"Confirm Password...")
    e3.bind("<Button-1>",sign)

        #====== Spin Box ========#
    sp = Spinbox(m, from_= 15, to = 100,width=10)
    sp.place(x=190,y=250)
    sp.insert(0, "Age")
    sp.bind("<FocusIn>",sign)

    #============= save / No ===========#


    
#========================= PAGE - 3[Password generater] ================#
def pass_word():
##    entry.delete(0, END)

    # Get the length of password
    var = IntVar()
    var1 = IntVar()
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = " "

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

    # Function for generation of password
def generate():
    password1 = low()
    entry.delete(0, END) # Clear entry before inserting new password
    entry.insert(0, password1)

    # Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    a1.copy(random_password)

    # Main Function
    # create GUI window
    var = IntVar()
    var1 = IntVar()

    # create label and entry to show
    # password generated

    Random_password = Label(m, text="Password")
    Random_password.grid(row=0)
    entry = Entry(m)
    entry.grid(row=0, column=1)

    # create label for length of password
    c_label = Label(m, text="Length")
    c_label.grid(row=1)

    # create Buttons Copy which will copy
    # password to clipboard and Generate
    # which will generate the password
    copy_button = Button(m, text="Copy", command=copy1)
    copy_button.grid(row=0, column=2)
    generate_button = Button(m, text="Generate", command=generate)
    generate_button.grid(row=0, column=3)

    # Radio Buttons for deciding the
    # strength of password
    # Default strength is Medium
    radio_low = Radiobutton(m, text="Low", variable=var, value=1)
    radio_low.grid(row=1, column=2, sticky='E')
    radio_middle = Radiobutton(m, text="Medium", variable=var, value=0)
    radio_middle.grid(row=1, column=3, sticky='E')
    radio_strong = Radiobutton(m, text="Strong", variable=var, value=3)
    radio_strong.grid(row=1, column=4, sticky='E')

    combo = Combobox(m, textvariable=var1)

    # Combo Box for length of your password
    combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
    combo.current(0)
    combo.grid(column=1, row=1)


#======================  [-->  Main * page  <--]  =========================#

def open():
    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    l1=Label(m,text="APP LOCK",font=('Castellar',33,'bold'))
    l1.place(x=190,y=90)
    a=Button(m,text="Login",font=('Illuma Black',15,"bold"),width=20,height=2,command=login,fg="yellow",bg='gray')
    a.place(x=190,y=200)
    b=Button(m,text="Signin",font=('Illuma Black',15,"bold"),width=20,height=2,command=sign,fg="red",bg='gray')
    b.place(x=190,y=290)
    c=Button(m,text="EXIT",font=('Illuma Black',15,"bold"),width=20,height=2,command=m.destroy,fg="black",bg='gray')
    c.place(x=190,y=380)
open()


###########################################################################################################





