#= = = = BOOK APPLICATION = = = = = = #
#          Project   By  Santhosh                   #
## = = = = = =>  Library  <= = = = = = = = ##  

import tkinter as tk
from tkinter import *
from tkinter import messagebox    
import subprocess as sp
from tkinter.ttk import Combobox
import random
import pyperclip
from tkcalendar import DateEntry
import subprocess as sp


 
## = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ##

# create the main window
m=tk.Tk()
m.title("|BooK ApplicatioN|")
m.geometry("600x600")

#======================  PAGE - 1 [Login]  =======================#

def sigup():
    
    global e1, e2, sp, var, cal, e3,bt

    b1 = Frame(m, width=600, height=600, bg='blue')
    m.Mframe = LabelFrame(m, width=600, height=600, font=('arial', 15, 'bold'), bg="light green", bd=15, relief='ridge')
    m.Mframe.grid(row=0, column=0, padx=2, pady=2)
    f1 = Frame(m, width=600, height=600, bg="gray")

    # ======= LABEL ======#

    l1 = Label(m, text="SIGNUP", font=('Copperplate Gothic Bold', 40, "bold"))
    l1.place(x=200, y=60)
    l2 = Label(m, text="Username:", font=('Times New Roman', 18, 'bold'))
    l2.place(x=50, y=150)
    l3 = Label(m, text="Password:", font=('Times New Roman', 18, 'bold'))
    l3.place(x=53, y=200)
    l4 = Label(m, text="Age:", font=('Times New Roman', 18, 'bold'))
    l4.place(x=110, y=250)
    l5 = Label(m, text="Gender:", font=('Times New Roman', 18, 'bold'))
    l5.place(x=70, y=300)
    l6 = Label(m, text="Date of Birth", font=('Times New Roman', 18, 'bold'))
    l6.place(x=40, y=350)
    l7 = Label(m, text="Confirm Password:", font=('Times New Roman', 18, 'bold'))
    l7.place(x=40, y=400)

    # ======== Radio Button =======#
    
    var = IntVar()
    Radiobutton(m, text="MALE", variable=var, value=1).place(x=190, y=300)
    Radiobutton(m, text="FEMALE", variable=var, value=2).place(x=280, y=300)
    Radiobutton(m, text="OTHERS", variable=var, value=3).place(x=380, y=300)

    # ======= Buttons =========#
    
    bt = Button(m, text="Continue", font=('Illuma Black', 20, "bold"), width=8, command=login, bg='green', fg='white',state="disabled")
    bt.place(x=400, y=490)

    bt_back = Button(m, text="Back", font=('Illuma Black', 20, "bold"), width=8, command=open, bg='red', fg='white')
    bt_back.place(x=50, y=490)

    bt_save = Button(m, text="Save", font=('Illuma Black', 20, "bold"), width=8, command=save_data, bg='blue', fg='white')
    bt_save.place(x=230, y=490)

    # ========  Entry Box  =========#

    e1 = Entry(m, width=30)
    e1.place(x=190, y=150)

    e2 = Entry(m, width=30)
    e2.place(x=190, y=200)

    e3 = Entry(m, width=25)
    e3.place(x=300, y=400)

    # ====== Spin Box ========#
    
    sp = Spinbox(m, from_=10, to=100, width=10)
    sp.place(x=190, y=250)

    # ====== DOB Box ======#
    # Create a Calendar using DateEntry
    cal = DateEntry(m, width=16, background="magenta3", foreground="white", bd=2)
    cal.place(x=200, y=350)

def save_data():

    global e1, e2, sp, var, cal,e3, bt

    username = e1.get()
    password = e2.get()
    age = sp.get()
    gender = var.get()
    dob = cal.get()
    confpass = e3.get()
    
    if not username:
        messagebox.showwarning("Warning", "Please enter UserName")
        bt.config(state="disabled")
    elif not password:
        messagebox.showwarning("Warning", "Please enter Password")
        bt.config(state="disabled")
    elif not age:
        messagebox.showwarning("Warning", "Please enter Age")
        bt.config(state="disabled")
    elif not gender:
        messagebox.showwarning("Warning", "Please enter Gender")
        bt.config(state="disabled")
    elif not dob:
        messagebox.showwarning("Warning", "Please enter DOB")
        bt.config(state="disabled")
    elif not confpass:
        messagebox.showwarning("Warning", "Please enter Confirm Password")
        bt.config(state="disabled")
    elif password != confpass:
        messagebox.showwarning("Warning", "Please ensure the passwords match")
        bt.config(state="disabled")
    else:
        messagebox.showinfo("Success", "Signup successful! Back to Login!")
        bt.config(state="normal")

#===========================  PAGE - 2  ========================#

def login():
    m.Mframe = LabelFrame(m, width=600, height=600, font=('arial', 15, 'bold'), bg="light green", bd=15, relief='ridge')
    m.Mframe.grid(row=0, column=0, padx=2, pady=2)
    f1 = Frame(m, width=600, height=600, bg="gray")

    # Labels
    l1 = Label(m, text="Login", font=('Copperplate Gothic Bold', 40, "bold"))
    l1.place(x=230, y=80)
    l2 = Label(m, text="Username:", font=('Times New Roman', 17, 'bold'))
    l2.place(x=140, y=180)
    l3 = Label(m, text="Password:", font=('Times New Roman', 17, 'bold'))
    l3.place(x=140, y=240)

    # Entry boxes
    e1 = StringVar()
    e2 = StringVar()
    e1_entry = Entry(m, width=23, textvariable=e1)
    e1_entry.place(x=280, y=186)
    e2_entry = Entry(m, width=23, textvariable=e2)
    e2_entry.place(x=280, y=240)

    def login_clicked():
        username = e1.get()
        password = e2.get()

        if username == "santhosh" and password == "1234":
            messagebox.showinfo("Login", "Login Successful")
            bt1.config(state="normal")  
        elif username != "santhosh":
            messagebox.showwarning("Login", "Incorrect username. Please try again.")
            bt1.config(state="disabled")  
        elif password != "1234":
            messagebox.showwarning("Login", "Incorrect password. Please try again.")
            bt1.config(state="disabled") 
        else:
            messagebox.showwarning("Login", "Incorrect username or password. Please try again.")
            bt1.config(state="disabled")  

    def reset_fields():
        e1.set("")
        e2.set("")
        bt1.config(state="disabled")

    bt_reset = Button(m, text="Reset", font=('Illuma Black', 15, "bold"), width=10, height=1, command=reset_fields, fg="white", bg='blue')
    bt_reset.place(x=400, y=330)
    
    bt1 = Button(m, text="Continue", font=('Illuma Black', 15, "bold"), width=10, bg='green', fg='white', command=Book_page,state="disabled")
    bt1.place(x=400, y=420)

    bt2 = Button(m, text="Back", font=('Illuma Black', 15, "bold"), width=10, height=1, command=open, fg="white", bg='red')
    bt2.place(x=100, y=420)

    bt3 = Button(m, text="Conform", font=('Illuma Black', 15, "bold"), width=10, height=1, command=login_clicked, fg="black",bg='white')
    bt3.place(x=250, y=330)

#======================== >  BooK PagE  < ====================#

def Book_page():
    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)

    w=Label(m,text='PROGRAMING BOOKS',font=('arial',30,'bold'),bg="lightgreen",bd=10) 
    w.place(x=80,y=20)

    b1=Button(m,text="1.Python",font=('Bookman Old Style',20,'bold'),bg="#6d9eeb",bd=10,command=Python_book)
    b1.place(x=190,y=100)

    b2=Button(m,text="2.Java",font=('Bookman Old Style',20,'bold'),bg="#6d9eeb",bd=10,command=Java_book)
    b2.place(x=190,y=180)

    b3=Button(m,text="3.SQL",font=('Bookman Old Style',20,'bold'),bg="#6d9eeb",bd=10,command=SQL_book)
    b3.place(x=190,y=260)

    b4=Button(m,text="4.HTML",font=('Bookman Old Style',20,'bold'),bg="#6d9eeb",bd=10,command=HTML_book)
    b4.place(x=190,y=340)

    b5=Button(m,text="5.CSS",font=('Bookman Old Style',20,'bold'),bg="#6d9eeb",bd=10,command=CSS_book)
    b5.place(x=190,y=420)

    b6=Button(m,text="EXIT",font=('Illuma Black',15,'bold'),command=m.destroy,bg="gray",bd=5)
    b6.place(x=250,y=520)

#========     =====   ===>  Python_Book  <===  =====     =========#

def Python_book():

    def update_button_state(event):
        selected_indices = listbox.curselection()
        if selected_indices:
            button.config(state="normal")
        else:
            button.config(state="disabled")

    def open_book():
        selected_index = listbox.curselection()[0]
        if selected_index == 0:
            book1()
        elif selected_index == 1:
            book2()
        elif selected_index == 2:
            book3()
        elif selected_index == 3:
            book4()
        elif selected_index == 4:
            book5()
        elif selected_index == 5:
            book6()

    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)

    tab = Label(m, text="Python Book", font=("Arial", 30, "bold"), bg="#ffcc00", fg="black")
    tab.place(x=210,y=20)

    label1 = Label(m, text="Select The Topic", font=("Arial", 15, "bold"), bg="#ffcc00", fg="black")
    label1.place(x=230,y=80)

    listbox = Listbox(m, height=6, width=16, bg="sky blue", activestyle='dotbox', font=("Helvetica",20,"bold"), fg="black")
    listbox.insert(1, "1.Introduction")
    listbox.insert(2, "2.Data Types")
    listbox.insert(3, "3.Data Structures")
    listbox.insert(4, "4.OOPS")
    listbox.insert(5, "5.NumPy")
    listbox.insert(6, "6.Pandas")
    listbox.place(x=200,y=150)

    listbox.bind("<<ListboxSelect>>", update_button_state)

    button = Button(m, text="Click", bg="green", font=('Illuma Black',20,'bold'), command=open_book,state="disable")
    button.place(x=270, y=420)

    bt = Button(m, text="Back", font=('Illuma Black',15,"bold"), width=10, command=Book_page, bg='red', fg='white')
    bt.place(x=100, y=450)

    bt = Button(m, text="Exit", font=('Illuma Black',15,'bold'), width=10, command=m.destroy, bg="gray")
    bt.place(x=400, y=450)

#==============  =======>  Python Note  <=======  ================#
def book1():
    a = "notepad.exe"
    filename = "book1.txt"
    sp.Popen([a, filename])

def book2():
    b = "notepad.exe"
    filename = "book2.txt"
    sp.Popen([b, filename])

def book3():
    c= "notepad.exe"
    filename = "book3.txt"
    sp.Popen([c, filename])

def book4():
    d = "notepad.exe"
    filename = "book4.txt"
    sp.Popen([d, filename])

def book5():
    e = "notepad.exe"
    filename = "book5.txt"
    sp.Popen([e, filename])

def book6():
    f = "notepad.exe"
    filename = "book6.txt"
    sp.Popen([f, filename])

#========     =====   ===>  Java_Book  <===  =====     =========#

def Java_book():
    def update_button_state(event):
        selected_indices = listbox.curselection()
        if selected_indices:
            button.config(state="normal")
        else:
            button.config(state="disabled")

    def open_book():
        selected_index = listbox.curselection()[0]
        if selected_index == 0:
            jbook1()
        elif selected_index == 1:
            jbook2()
        elif selected_index == 2:
            jbook3()
        elif selected_index == 3:
            jbook4()
        elif selected_index == 4:
            jbook5()
        elif selected_index == 5:
            jbook6()

    m.Mframe = LabelFrame(m, width=600, height=600, font=('arial', 15, 'bold'), bg="light green", bd=15, relief='ridge')
    m.Mframe.grid(row=0, column=0, padx=2, pady=2)

    tab = Label(m, text="Java Book", font=("Arial", 30, "bold"), bg="#ffcc00", fg="black")
    tab.place(x=210, y=20)

    label1 = Label(m, text="Select The Topic", font=("Arial", 15, "bold"), bg="#ffcc00", fg="black")
    label1.place(x=230, y=80)

    listbox = Listbox(m, height=6, width=19, bg="sky blue", activestyle='dotbox', font=("Helvetica", 20, "bold"), fg="black")
    listbox.insert(1, "1.Introduction")
    listbox.insert(2, "2.Data Types")
    listbox.insert(3, "3.String/Array")
    listbox.insert(4, "4.Exception Handling")
    listbox.insert(5, "5.Interface")
    listbox.insert(5, "6.Generics")
    listbox.place(x=180, y=150)

    listbox.bind("<<ListboxSelect>>", update_button_state)

    button = Button(m, text="Click", bg="green", font=('Illuma Black', 20, 'bold'), command=open_book, state="disabled")
    button.place(x=270, y=420)

    bt = Button(m, text="Back", font=('Illuma Black', 15, "bold"), width=10, command=Book_page, bg='red', fg='white')
    bt.place(x=100, y=450)

    bt = Button(m, text="Exit", font=('Illuma Black', 15, 'bold'), width=10, command=m.destroy, bg="gray")
    bt.place(x=400, y=450)


#==============  =======>  Java Note  <=======  ================#
def jbook1():
    filename = "jbook1.txt"
    sp.Popen(["notepad.exe", filename])

def jbook2():
    filename = "jbook2.txt"
    sp.Popen(["notepad.exe", filename])

def jbook3():
    filename = "jbook3.txt"
    sp.Popen(["notepad.exe", filename])

def jbook4():
    filename = "jbook4.txt"
    sp.Popen(["notepad.exe", filename])

def jbook5():
    filename = "jbook5.txt"
    sp.Popen(["notepad.exe", filename])

def jbook6():
    filename = "jbook6.txt"
    sp.Popen(["notepad.exe", filename])

#========     =====   ===>  SQL_Book  <===  =====     =========#
    
def SQL_book():
    
    def update_button_state(event):
        selected_indices = listbox.curselection()
        if selected_indices:
            button.config(state="normal")
        else:
            button.config(state="disabled")

    def open_book():
        selected_index = listbox.curselection()[0]
        if selected_index == 0:
            sbook1()
        elif selected_index == 1:
            sbook2()
        elif selected_index == 2:
            sbook3()
        elif selected_index == 3:
            sbook4()
        elif selected_index == 4:
            sbook5()
        elif selected_index == 5:
            sbook6()

    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    
    tab = Label(m, text="SQL Books", font=("Arial", 30, "bold"), bg="#ffcc00", fg="black")
    tab.place(x=210,y=20)

    label1 = Label(m, text="Select The Topic", font=("Arial", 15, "bold"), bg="#ffcc00", fg="black")
    label1.place(x=230,y=80)

    listbox = Listbox(m, height=6, width=27, bg="sky blue", activestyle='dotbox', font=("Helvetica",20,"bold"), fg="black")
    listbox.insert(1, "1.Introduction")
    listbox.insert(1, "2.Data Definition Language")
    listbox.insert(2, "3.Data Manipulation Language")
    listbox.insert(3, "4.Querying with SQL")
    listbox.insert(4, "5.Database Joins")
    listbox.insert(5, "6.Database Normalization")
    listbox.place(x=100,y=150)
    listbox.bind("<<ListboxSelect>>", update_button_state)

    button = Button(m, text="Click", bg="green",font=('Illuma Black',20,'bold'),command=open_book,state="disable")
    button.place(x=270, y=420)

    bt=Button(m,text="Back",font=('Illuma Black',15,"bold"),width=10,command=Book_page,bg='red',fg='white')
    bt.place(x=100,y=450)
    
    bt=Button(m,text="Exit",font=('Illuma Black',15,'bold'),width=10,command=m.destroy,bg="gray",)
    bt.place(x=400,y=450)

#==============  =======>  SQL Note  <=======  ================#
def sbook1():
    filename = "sbook1.txt"
    sp.Popen(["notepad.exe", filename])

def sbook2():
    filename = "sbook2.txt"
    sp.Popen(["notepad.exe", filename])

def sbook3():
    filename = "sbook3.txt"
    sp.Popen(["notepad.exe", filename])

def sbook4():
    filename = "sbook4.txt"
    sp.Popen(["notepad.exe", filename])

def sbook5():
    filename = "sbook5.txt"
    sp.Popen(["notepad.exe", filename])

def sbook6():
    filename = "sbook6.txt"
    sp.Popen(["notepad.exe", filename])

#========     =====   ===>  HTML_Book  <===  =====     =========#
def HTML_book():

    def update_button_state(event):
        selected_indices = listbox.curselection()
        if selected_indices:
            button.config(state="normal")
        else:
            button.config(state="disabled")

    def open_book():
        selected_index = listbox.curselection()[0]
        if selected_index == 0:
            hbook1()
        elif selected_index == 1:
            hbook2()
        elif selected_index == 2:
            hbook3()
        elif selected_index == 3:
            hbook4()
        elif selected_index == 4:
            hbook5()
       
    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    
    tab = Label(m, text="HTML Book", font=("Arial", 30, "bold"), bg="#ffcc00", fg="black")
    tab.place(x=210,y=20)

    label1 = Label(m, text="Select The Topic", font=("Arial", 15, "bold"), bg="#ffcc00", fg="black")
    label1.place(x=230,y=80)

    listbox = Listbox(m, height=5, width=15, bg="sky blue", activestyle='dotbox', font=("Helvetica",20,"bold"), fg="black")
    listbox.insert(1, "1.Introduction")
    listbox.insert(2, "2.HTML Basics")
    listbox.insert(3, "3.HTML Forms")
    listbox.insert(4, "4.Web Design")
    listbox.insert(5, "5.Accessibility")
    listbox.place(x=190,y=150)

    listbox.bind("<<ListboxSelect>>", update_button_state)

    button = Button(m, text="Click", bg="green",font=('Bookman Old Style',20,'bold'),command=open_book,state="disable")
    button.place(x=270, y=420)

    bt=Button(m,text="Back",font=('Illuma Black',15,"bold"),width=10,command=Book_page,bg='red',fg='white')
    bt.place(x=100,y=450)
    
    bt=Button(m,text="Exit",font=('Illuma Black',15,'bold'),width=10,command=m.destroy,bg="gray",)
    bt.place(x=400,y=450)

#==============  =======>  HTML Note  <=======  ================#
def hbook1():
    filename = "hbook1.txt"
    sp.Popen(["notepad.exe", filename])

def hbook2():
    filename = "hbook2.txt"
    sp.Popen(["notepad.exe", filename])

def hbook3():
    filename = "hbook3.txt"
    sp.Popen(["notepad.exe", filename])

def hbook4():
    filename = "hbook4.txt"
    sp.Popen(["notepad.exe", filename])

def hbook5():
    filename = "hbook5.txt"
    sp.Popen(["notepad.exe", filename])

#========     =====   ===>  CSS_Book  <===  =====     =========#
def CSS_book():
    def update_button_state(event):
        selected_indices = listbox.curselection()
        if selected_indices:
            button.config(state="normal")
        else:
            button.config(state="disabled")

    def open_book():
        selected_index = listbox.curselection()[0]
        if selected_index == 0:
            cbook1()
        elif selected_index == 1:
            cbook2()
        elif selected_index == 2:
            cbook3()
        elif selected_index == 3:
            cbook4()
        elif selected_index == 4:
            cbook5()

    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    
    tab = Label(m, text="CSS Books", font=("Arial", 30, "bold"), bg="#ffcc00", fg="black")
    tab.place(x=210,y=20)

    label1 = Label(m, text="Select The Topic", font=("Arial", 15, "bold"), bg="#ffcc00", fg="black")
    label1.place(x=230,y=80)

    listbox = Listbox(m, height=5, width=15, bg="sky blue", activestyle='dotbox', font=("Helvetica",20,"bold"), fg="black")
    listbox.insert(1, "1.Introduction")
    listbox.insert(2, "2.Web Design")
    listbox.insert(3, "3.CSS3")
    listbox.insert(4, "4.CSS Grid")
    listbox.insert(5, "5.Preprocessors")
    listbox.place(x=200,y=150)

    listbox.bind("<<ListboxSelect>>", update_button_state)


    button = Button(m, text="Click", bg="green",font=('Illuma Black',20,'bold'),command=open_book,state="disable")
    button.place(x=270, y=420)

    bt=Button(m,text="Back",font=('Illuma Black',15,"bold"),width=10,command=Book_page,bg='red',fg='white')
    bt.place(x=100,y=450)
    
    bt=Button(m,text="Exit",font=('Illuma Black',15,'bold'),width=10,command=m.destroy,bg="gray",)
    bt.place(x=400,y=450)

#==============  =======>  CSS Note  <=======  ================#

def cbook1():
    filename = "cbook1.txt"
    sp.Popen(["notepad.exe", filename])

def cbook2():
    filename = "cbook2.txt"
    sp.Popen(["notepad.exe", filename])

def cbook3():
    filename = "cbook3.txt"
    sp.Popen(["notepad.exe", filename])

def cbook4():
    filename = "cbook4.txt"
    sp.Popen(["notepad.exe", filename])

def cbook5():
    filename = "cbook5.txt"
    sp.Popen(["notepad.exe", filename])

#======================  [-->  Main * Page  <--]  =========================#

def open():
    
    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="light green",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    
    l1=Label(m,text="BOOK APPLICATION",font=('Castellar',33,'bold'))
    l1.place(x=50,y=90)

    a=Button(m,text="Login",font=('Illuma Black',15,"bold"),width=20,height=2,command=login,fg="yellow",bg='gray')
    a.place(x=190,y=200)

    b=Button(m,text="Signin",font=('Illuma Black',15,"bold"),width=20,height=2,command=sigup,fg="red",bg='gray')
    b.place(x=190,y=290)

    c=Button(m,text="Exit",font=('Illuma Black',15,"bold"),width=20,height=2,command=m.destroy,fg="black",bg='gray')
    c.place(x=190,y=380)

open()

################################################################################################




