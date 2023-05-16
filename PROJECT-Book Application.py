import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox    
import subprocess as sp
#import pymysql


m=tk.Tk()
m.title("EMPLOYE PORTAL")
m.geometry("600x600")
#============Username=============#
e1=tk.StringVar()
e2=tk.StringVar()
#=================================#
##db_connection=pymysql.connect(
##    host="localhost",
##    user="root",
##    password="santhosh",
##    database="data"
##    )
##my_database=db_connection.cursor()
##print("Connected..")
##
##def db():
##    m.Mframe=LabelFrame(m,width=600,height=600,font=('arial',15,'bold'),bg="lightblue",bd=15,relief='ridge')
##    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
##    f1=Frame(m,width='600',height='600',bg="gray")
##    l1=Label(m,text="Username:",font=('Times New Roman',19,'bold')).place(x=100,y=200)
##    l2=Label(m,text="Pasword:",font=('Times New Roman',19,'bold')).place(x=100,y=255)
##    e1=Entry(m,width=25)
##    e1.place(x=280,y=210)
##    e2=Entry(m,width=25)
##    e2.place(x=280,y=260)
##    
##    def signup():
##            sql_statement="INSERT INTO santa(USER NAME,PASSWORD)value(%s,%s)"
##            values=(e1.get(),e2.get())
##            my_database.execute(sql_statement,values)
##            db_connection.commit()
##    bu=Button(m,text="submite",width=25,font=("arial",15),command=signup,bg="green",fg="white")
##    bu.place(x=200,y=350)
##    
##db()
##
##
##response = messagebox("data base", "sucessful to register")
##if response == True:
##    print("OK button clicked")
##elif response == False:
##    print("Cancel button clicked")
##
##if(e1.get()and e2.get()):
##    messagebox.showinfo("show","Register successfully") 
##elif(e1.get()!=e2.get()):
##    messagebox.showinfo("show","Wrong password")
##else:
##    messagebox.showinfo("show","Sorry try again....!")
##   
#=============================================SIGN UP====================================================#
def sign():
    b1=Frame(m,width='800',height='800',bg='blue')
    m.Mframe=LabelFrame(m,width=800,height=800,font=('arial',15,'bold'),bg="lightblue",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    f1=Frame(m,width='800',height='800',bg="gray")
    l1=Label(m,text="SIGNUP:",font=('Illuma Black',40,"bold")).place(x=300,y=100)
    l2=Label(m,text="Username:",font=('Times New Roman',20,'bold')).place(x=100,y=200)
    l3=Label(m,text="Password:",font=('Times New Roman',20,'bold')).place(x=100,y=255)
    l4=Label(m,text="Age:",font=('Times New Roman',20,'bold')).place(x=100,y=300)
    l5=Label(m,text="Gender:",font=('Times New Roman',20,'bold')).place(x=100,y=350)
    vars=IntVar()
    Radiobutton(m,text="MALE",variable=vars,value=1).place(x=400,y=350)
    Radiobutton(m,text="FEMALE",variable=vars,value=2).place(x=485,y=350)
    Radiobutton(m,text="OTHERS",variable=vars,value=3).place(x=585,y=350)
    e1=Entry(m,width=30)
    e1.place(x=400,y=210)
    e2=Entry(m,width=30)
    e2.place(x=400,y=260)
    e3=Entry(m,width=30)
    e3.place(x=400,y=310)
    bt=Button(m,text="continue",font=('Illuma Black',20,"bold"),width=30,command=frame,bg='green',fg='white')
    bt.place(x=200,y=490)

#=============================================LOGIN======================================================#
def login():
    b2 = Frame(m, width=800, height=800, bg='blue')
    m.Mframe = LabelFrame(m, width=800, height=800, font=('arial', 15, 'bold'), bg="lightblue", bd=15, relief='ridge')
    m.Mframe.grid(row=0, column=0, padx=2, pady=2)
    f2 = Frame(m, width=800, height=800, bg="gray")
    l1 = Label(m, text="Login", font=('Illuma Black', 40, "bold"))
    l1.place(x=350, y=140)
    l2 = Label(m, text="Username:", font=('algerian', 17, 'bold'))
    l2.place(x=200, y=300)
    l3 = Label(m, text="Password:", font=('algerian', 17, 'bold'))
    l3.place(x=200, y=370)
    e1 = StringVar()
    e2 = StringVar()
    e1_entry = Entry(m, width=28, textvariable=e1)
    e1_entry.place(x=400, y=370)
    e2_entry = Entry(m, width=28, textvariable=e2)
    e2_entry.place(x=400, y=300)
    bt1 = Button(m, text="continue", font=('Illuma Black', 15, "bold"), width=25, command=frame, bg='green', fg='white')
    bt1.place(x=290, y=500)
    bt2 = Button(m, text="EXIT", font=('Illuma Black', 15, "bold"), width=20, height=2, command=m.destroy, fg="black", bg='gray')
    bt2.place(x=350, y=680)

#==============================================MAIN OPEN=======================================================#
def open():
    m.Mframe=LabelFrame(m,width=650,height=650,font=('arial',15,'bold'),bg="lightblue",bd=15,relief='ridge')
    m.Mframe.grid(row=0,column=0,padx=2,pady=2)
    l1=Label(m,text="EMPLOYE PORTAL",font=('Castellar',30,'bold')).place(x=150,y=90)
    a=Button(m,text="Login",font=('Illuma Black',15,"bold"),width=20,height=2,command=login,fg="yellow",bg='gray')
    a.place(x=200,y=200)
    b=Button(m,text="Signin",font=('Illuma Black',15,"bold"),width=20,height=2,command=sign,fg="red",bg='gray')
    b.place(x=200,y=290)
    c=Button(m,text="EXIT",font=('Illuma Black',15,"bold"),width=20,height=2,command=m.destroy,fg="black",bg='gray')
    c.place(x=200,y=380)
open()


#=================================================================================================================#

















        
   



