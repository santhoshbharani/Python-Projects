from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def mark():
    
    # Check if user has entered a value in the Entry box
    if entry.get() == "":
        messagebox.showwarning("Error", "select")
    else:
        mark = int(entry.get())
        selected_subject = listbox.curselection()

        if selected_subject:
            subject_index = selected_subject[0]
            subject = listbox.get(subject_index)

            if subject in ('Tamil','English','Maths','Science','Social'):
                if mark > 90:
                    messagebox.showinfo("Result", "Excellent")
                elif mark > 70:
                    messagebox.showinfo("Result", "Good")
                elif mark > 50:
                    messagebox.showinfo("Result", "Pass")
                elif mark > 35:
                    messagebox.showinfo("Result", "Deii parama padi da")
                else:
                    messagebox.showinfo("Result", "Odi poiru nee fail uh..!!")
        else:
            messagebox.showwarning("Error", "Please select a subject")

window = Tk()
window.geometry("500x500")
window.title("Label and Button")

##window.f1 = LabelFrame(window, width=500, height=500, font=('arial', 15, 'bold'), bg="light green", bd=15, relief='ridge')
##window.f1.grid(padx=2, pady=2)


# Adding the background image
bg_img = Image.open("background.jpg")
bg_img = bg_img.resize((500, 500), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg_img)
canvas1 = Canvas(window, width=500, height=500)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

tab = Label(window, text="LKG SCHOOL", font=("Arial", 12, "bold"), bg="#ffcc00", fg="black")
tab.pack()

label1 = Label(window, text="Select The Subject", font=("Arial", 12, "bold"), bg="#ffcc00", fg="black")
label1.pack()

entry = Entry(window)
entry.pack()
entry.place(x=160, y=370)

listbox = Listbox(window, height=10, width=15, bg="sky blue", activestyle='dotbox', font="Helvetica", fg="black")
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
