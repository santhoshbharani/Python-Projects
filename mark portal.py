from tkinter import *
from tkinter import messagebox

def mark():
    
    # Check if user has entered a value in the Entry box
    if entry.get() == "":
        messagebox.showwarning("Error", "Entry  Your your Mark")
    else:
        mark = int(entry.get())
        selected_subject = listbox.curselection()

        if selected_subject:
            subject_index = selected_subject[0]
            subject = listbox.get(subject_index)

            if subject in ('Tamil','English','Maths','Science','Social'):
                if mark==100:
                    messagebox.showinfo("Result", "Congratulations...!")
                elif mark > 90:
                    messagebox.showinfo("Result", "Excellent")
                elif mark > 70:
                    messagebox.showinfo("Result", "Good")
                elif mark > 50:
                    messagebox.showinfo("Result", "Pass")
                elif mark > 35:
                    messagebox.showinfo("Result", "Need More to Study")
                else:
                    messagebox.showinfo("Result", "Fail.. Read well keep To Study..,")
        else:
            messagebox.showwarning("Error", "Select Your Subject")

window = Tk()
window.geometry("500x500")
window.title("Mark Result")

tab = Label(window, text="LKG SCHOOL", font=("Arial", 12, "bold"), bg="#ffcc00", fg="black")
tab.pack()

label1 = Label(window, text="Select The Subject", font=("Arial", 12, "bold"), bg="#ffcc00", fg="black")
label1.pack()

entry = Entry(window, background="gold")
entry.pack()
entry.place(x=160, y=370)

listbox = Listbox(window, height=7, width=8, bg="sky blue", activestyle='dotbox', font=("Helvetica",20,"bold"), fg="black")
label = Label(window, text="Subjects")
listbox.insert(1, "Tamil")
listbox.insert(2, "English")
listbox.insert(3, "Maths")
listbox.insert(4, "Science")
listbox.insert(5, "Social")
label.pack()
listbox.pack()

button = Button(window, text="Click", bg="green", command=mark)
button.pack()
button.place(x=220, y=420)

window.mainloop()
