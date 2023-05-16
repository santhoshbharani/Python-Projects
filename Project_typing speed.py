from tkinter import *
import random
from timeit import default_timer 
import difflib
 
print("----------- Python Typing Speed test ------------")
 
root=Tk()
root.title('Typing test')
root.geometry("700x700")
 
entered=StringVar() 
 
b1=Frame(root,width='700',height='700',bg='gold')
root.Mframe=LabelFrame(root,width=700,height=700,font=('arial',15,'bold'),bg="gold",bd=15,relief='ridge')
root.Mframe.grid(row=0,column=0,padx=2,pady=2)

greet = Label(root, font = ('arial', 30, 'bold'), text = "Welcome to Ts..!")
greet.place(x=190,y=50)
 
words=['We are developing project', 'This is Windows Os', 'We are Hiring', 'Lets Play a game','Python is a language', 'We love Coding', 'This is an amazing Article', 'I am an Intern', 'Lets check the Output', 'we are Compiling this program' ]
word=random.choice(words)
 
def check():
    global entered
    global word
    global start
 
    string=f"{entered.get()}"
    end=  default_timer()
    time= round(end-start,2)
    print(time)
    speed=round(len(word.split())*60/time,2)
    print(speed)
 
    if string==word:
        Msg1 ="Time= " + str(time) + ' seconds'
        Msg2=" Accuracy= 100% "
        Msg3= " Speed= " + str(speed) + 'wpm' 
 
    else:
        accuracy=difflib.SequenceMatcher(None,word,string).ratio()
        accuracy=str(round(accuracy*100,2))
        Msg1 ="Time= "+ str(time) + ' seconds'
        Msg2=" Accuracy= " + accuracy + '%'
        Msg3= " Speed= " + str(speed) + ' wpm' #words per minute 
 
    
    label=Label(root, font = ('arial', 15, 'bold'), text = Msg1)
    label.place(x=250,y=300)
 
    label=Label(root, font = ('arial', 15, 'bold'), text = Msg2)
    label.place(x=250,y=350)
 
    label=Label(root, font = ('arial', 15, 'bold'), text = Msg3)
    label.place(x=250,y=400)

   
def play():
    global word
    global start
    global entered  
 
label=Label(root, font = ('arial', 15), text = "Type here:")
label.place(x=100,y=250)

entered=StringVar() 
enter=Entry(root,textvariable=entered,font =('arial', 15),width=25)
enter.place(x=250,y=250)

btn = Button(root,text="Check",command=check,font=('Illuma Black',15,"bold"),width=15,height=1,fg="green",bg='white')
btn.place(x=250,y=500)


label=Label(root, font = ('arial', 20, 'bold'), text = word)  #we calling the words
label.place(x=50,y=150)

btn = Button(root,text="Reset",command=play,font=('Illuma Black',15,"bold"),width=15,height=1,fg="red",bg='white')
btn.place(x=250,y=550)

c=Button(root,text="Exit",font=('Illuma Black',15,"bold"),width=15,height=1,command=root.destroy,fg="black",bg='gray')
c.place(x=250,y=600)

start= default_timer()
 
mainloop()
