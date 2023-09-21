#=== > Project_Deployement < ===#
#                               #
#===============================#

#=========} Python Lib {===========#
from tkinter import *
from tkinter import ttk
import tkinter as tk

import numpy as np
import pandas as pd
from tkinter import filedialog
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#= = = = > ML algorithms < = = = = #

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


#**********************************************************#

class base():
    def init(self):
        print("Base started")

    def base_fn(self):
        ob = home_page()
        ob.home_fn()

class home_page(base):
    global data, path

    def home_fn(self):
        global x_index, y_index, selected_x, selected_y
        x_index = []
        y_index = []
        selected_x = []
        selected_y = [] 
        
        def select_x_fn():
            # Here the selected one from the combobox will get and located the index num in dataset and the index num will be appended in list_index as X var
            x = select_col.get()
            # print("selected column = ",x)
            selected_x.append(x)

            ind_x = data.columns.get_loc(x)
            # print("X cols-------->",ind_x)
            x_index.append(ind_x)

            # inserting to the text box
            x_txt_box.insert(END, x + '\n')

        def select_y_fn():
            # Here the selected one from the combobox will get and located the index num in dataset and the index num will be appended in list_index as X var
            y = select_col.get()
            selected_y.append(y)
            # print("selected column = ",y)
            ind_y = data.columns.get_loc(y)
            # print("Y cols-------->",ind_y)
            y_index.append(ind_y)
            y_txt_box.insert(END, y + '\n')

        def page_2_fn():
            # this fn to
            # print(list_index)
            x_col = x_index
            y_col = y_index
            name_x = selected_x
            name_y = selected_y
            win.destroy()
            obj = algorithm_choose()
            obj.algorithms(path, x_col, y_col, name_x, name_y)

        def open_file_fn():
            global path, data
            file = filedialog.askopenfilename(title="Open File", filetypes=(
            ("csv files", "*.csv"), ("Text Files", "*.txt"), ("All files", "*."), ("Python files", "*.py")))
            #print(file)
            
            path = file.replace("/", "//")
            # print(path)
            data = pd.read_csv(path)
            list_1 = list(data.columns)
            #print(list_1)
            select_col['values'] = tuple(list_1)

        def refresh_fn():
            x_txt_box.delete('1.0', END)
            y_txt_box.delete('1.0', END)
            y_index.clear()
            x_index.clear()
            selected_x.clear()
            selected_y.clear()
        
        # Page_1
        win = tk.Tk()
        win.geometry('1400x1000')
        win.title("Prediction Algorithms")
        
        
        
        frame1 = tk.Frame(win, bg='sky blue',bd=15,relief='ridge')
        frame1.pack(ipadx=50, ipady=50, expand=True, fill='both')
        
        header_l = tk.Label(frame1, text='DEPLOYMENT', font=("Futura", "30", "bold"), bg='white', relief=RAISED)
        header_l.place(x=550, y=10)
        
        select_col_en = tk.StringVar()
        select_col = ttk.Combobox(frame1, width=46, textvariable=select_col_en)
        select_col.place(x=500, y=180)
        
        select_x_btn = tk.Button(frame1,font=('Illuma Black',15,"bold"),text='Independent X', relief=RAISED,fg="red", command=select_x_fn, width=13,bd=5,bg='white')
        select_x_btn.place(x=325, y=450)
        
        choose1 = tk.Label(frame1, text="Independent X", font=("Futura", "16", "bold"), bg='white', relief=RAISED)
        choose1.place(x=320, y=380)
        
        select_y_btn = tk.Button(frame1,font=('Illuma Black',15,"bold"), text='Dependent Y', relief=RAISED, fg="red",command=select_y_fn, width=13,bd=5,bg='white')
        select_y_btn.place(x=900, y=450)
        
        choose2 = tk.Label(frame1, text="Dependent Y", font=("Futura", "16", "bold"), bg='white', relief=RAISED)
        choose2.place(x=900, y=380)
        
        x_txt_box = tk.Text(frame1, font=("Futura", '15', "bold"), width=23, height=8)
        x_txt_box.place(x=280, y=520)
        
        y_txt_box = tk.Text(frame1, font=("Futura", '15', "bold"), width=23, height=8)
        y_txt_box.place(x=850, y=520)
        
        choose = tk.Label(frame1, text="Choose the Data set", font=("Futura", "16", "bold"), bg='white', relief=RAISED)
        choose.place(x=600, y=100)
        
        next_btn = tk.Button(frame1,font=('Illuma Black',15,"bold"),text='Next', relief=RAISED,fg="Green", command=page_2_fn, width=10,bd=5,bg='white')
        next_btn.place(x=830, y=260)
        
        refresh_btn = tk.Button(frame1,font=('Illuma Black',15,"bold"),text='Refresh', relief=RAISED,fg="blue", command=refresh_fn, width=10,bd=5,bg='white')
        refresh_btn.place(x=650, y=260)
        
        open_btn = tk.Button(frame1,font=('Illuma Black',15,"bold"), text='Open', relief=RAISED,fg="black", command=open_file_fn, width=10, bg='white',bd=5)
        open_btn.place(x=470, y=260)
    
        exit_btn=Button(frame1,text="EXIT",font=('Illuma Black',15,'bold'),command=frame1.destroy,bg="gray",bd=5)
        exit_btn.place(x=650,y=600)
        
        win.mainloop()
        
class algorithm_choose(home_page):

    def algorithms(self, path, x_col, y_col, name_x, name_y):
        win1 = Tk()
        win1.geometry('1400x1000')
        # win1.state('zoomed')
        win1.title("Prediction Algorithms")
        win1.config(background='black')
        frame2 = Frame(win1,bg='sky blue',bd=15,relief='ridge')
        frame2.pack(ipadx=50, ipady=50, expand=True, fill='both')
        #-------------------Regression------------------------------#
        def slin_reg_fn():  # Simple linear regression

            frame2.destroy()

            header_l = Label(win1, text='Simple-Linear Regression', font=("Futura", "28", "bold"), bg='red',
                             relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame5 = Frame(win1, bg='lightgreen')
            frame5.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_slin_reg_fn():  # Simple linear regression model
                entry = col_1_e.get()
                # print(path, x_col, y_col,name_x,name_y)

                # Train splitting
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

                # Training model
                regressor = LinearRegression()
                regressor.fit(x_train, y_train)

                y_pred = regressor.predict(x_test)
                pred_y = regressor.predict([[entry]])
                print(pred_y)

                scc=regressor.score(x_test,y_test)
                print(scc)
                
                from sklearn.metrics import r2_score
                scr2=r2_score(y_test,y_pred)

                pred_l = Label(frame5, text=pred_y[0][0].round(2), font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=620, y=250)
                
                score3 = Label(frame5, text=scr2, font=("Futura", "18", "bold"), bg='light grey')
                score3.place(x=620, y=350)

            col_1_l = Label(frame5, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=370, y=150)

            col_1_en = StringVar()
            col_1_e = Entry(frame5, width=20, textvariable=col_1_en)
            col_1_e.place(x=620, y=150)

            result_l = Label(frame5, text=f"{name_y[0]}", font=("Futura", "18", "bold"), bg='light grey')
            result_l.place(x=370, y=250)
            
            score = Label(frame5, text="Score", font=("Futura", "18", "bold"), bg='light grey')
            score.place(x=370, y=350)

            result_btn = Button(frame5, text='Predict', bg='light grey', relief=GROOVE, command=pred_slin_reg_fn)
            result_btn.place(x=510, y=450)

        def mlin_reg_fn():  # Multi linear regression
            frame2.destroy()

            header_l = Label(win1, text='Multi-Linear Regression', font=("Futura", "28", "bold"), bg='red',
                             relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame6 = Frame(win1, bg='lightblue')
            frame6.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_mlin_reg_fn():  # Multi linear regression Model

                entry1 = col_1_e.get()
                entry2 = col_2_e.get()

                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

                regressor = LinearRegression()
                regressor.fit(x_train, y_train)

                y_pred = regressor.predict(x_test)
                # print(y_pred)

                pred_y = regressor.predict([[entry1, entry2]])
                print(pred_y)
                
                from sklearn.metrics import r2_score
                scr2=r2_score(y_test,y_pred)
                
                score3 = Label(frame6, text=scr2, font=("Futura", "12", "bold"), bg='light grey')
                score3.place(x=600, y=370)
                
                pred_l = Label(frame6, text=pred_y[0][0].round(2), font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=300)

            col_1_l = Label(frame6, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)

            col_2_l = Label(frame6, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=210)

            col_3_l = Label(frame6, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=300)
            
            score = Label(frame6, text="Score", font=("Futura", "12", "bold"), bg='light grey',width=12)
            score.place(x=330, y=370)
            
            col_1_en = StringVar()
            col_1_e = Entry(frame6, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=155)

            col_2_en = StringVar()
            col_2_e = Entry(frame6, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=210)

            result_btn = Button(frame6, text='Predict', bg='light grey', relief=GROOVE,width=12, command=pred_mlin_reg_fn)
            result_btn.place(x=460, y=430)

        def plin_reg_fn():
            frame2.destroy()

            header_l = Label(win1, text='Polynomial Regression', font=("Futura", "28", "bold"), bg='red', relief=RAISED,
                             padx=6)
            header_l.pack(ipady=10)

            frame7 = Frame(win1, bg='')
            frame7.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_poly_reg_fn():
                x_entry = col_1_e.get()
                poly_reg = PolynomialFeatures(degree=7)
                x1 = poly_reg.fit_transform(x)

                regressor = LinearRegression()
                regressor.fit(x1, y)

                pred_y = regressor.predict(poly_reg.fit_transform([[x_entry]]))
                print(pred_y)
                
                from sklearn.metrics import r2_score
                scr2=r2_score(y_test,y_pred)
                
                score3 = Label(frame7, text=scr2, font=("Futura", "12", "bold"), bg='light grey')
                score3.place(x=600, y=370)

                pred_l = Label(frame7, text=pred_y[0][0].round(2), font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)

            col_1_l = Label(frame7, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)

            col_1_en = StringVar()
            col_1_e = Entry(frame7, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=155)
            
            score = Label(frame7, text="Score", font=("Futura", "12", "bold"), bg='light grey',width=12)
            score.place(x=330, y=370)
            
            result_l = Label(frame7, text=f"{name_y[0]}", font=("Futura", "18", "bold"), bg='light grey')
            result_l.place(x=350, y=250)

            result_btn = Button(frame7, text='Predict', bg='light grey', relief=GROOVE, command=pred_poly_reg_fn)
            result_btn.place(x=460, y=425)
            
        def svr_reg_fn():
            frame2.destroy()

            header_l = Label(win1, text='Support Vector Regression', font=("Futura", "28", "bold"), bg='red', relief=RAISED,
                             padx=6)
            header_l.pack(ipady=10)

            frame13 = Frame(win1, bg='purple')
            frame13.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_svr_reg_fn():
                entry1 = col_1_e.get()
                entry2 = col_2_e.get()
                 
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
                 
                from sklearn.svm import SVR
                regressor = SVR(kernel='linear')  # You can choose different kernels (e.g., 'linear', 'rbf', etc.) as per your requirement
                regressor.fit(x_train, y_train)
                 
                y_pred = regressor.predict(x_test)
                # print(y_pred)
                 
                pred_y = regressor.predict([[entry1, entry2]])
                print(pred_y)
                 
                from sklearn.metrics import r2_score
                scr2 = r2_score(y_test, y_pred)
                print(scr2)
        
            
                score3 = Label(frame13, text=scr2, font=("Futura", "12", "bold"), bg='light grey')
                score3.place(x=600, y=300)

                pred_l = Label(frame13, text=pred_y[0], font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)

            col_1_l = Label(frame13, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)

            col_2_l = Label(frame13, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)

            col_3_l = Label(frame13, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
            
            score = Label(frame13, text="Score", font=("Futura", "12", "bold"), bg='light grey',width=12)
            score.place(x=350, y=300)
            
            col_1_en = StringVar()
            col_1_e = Entry(frame13, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)

            col_2_en = StringVar()
            col_2_e = Entry(frame13, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)


            result_btn = Button(frame13, text='Predict', bg='light grey', relief=GROOVE, command=pred_svr_reg_fn)
            result_btn.place(x=460, y=425)
            
        def dcr_reg_fn():
            frame2.destroy()

            header_l = Label(win1, text='Decision Tree Regression', font=("Futura", "28", "bold"), bg='red', relief=RAISED,
                             padx=6)
            header_l.pack(ipady=10)

            frame15 = Frame(win1, bg='yellow')
            frame15.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_dcr_reg_fn():
                

                # Split the data into training and testing sets
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
                
                # Create and train the Decision Tree regressor
                regressor = DecisionTreeRegressor(random_state=0)
                regressor.fit(x_train, y_train)
                
                # Make predictions on the testing set
                y_pred = regressor.predict(x_test)
                
                # Print the predictions for the test set
                print(y_pred)
                
                # Make predictions on new data
                entry1 = col_1_e.get()
                entry2 = col_2_e.get()
                pred_y = regressor.predict([[entry1, entry2]])
                print(pred_y)
                
                # Calculate the R-squared score (coefficient of determination)
                r2 = r2_score(y_test, y_pred)
                print("R-squared Score:", r2)

        
            
                score3 = Label(frame15, text=r2, font=("Futura", "12", "bold"), bg='light grey')
                score3.place(x=600, y=300)

                pred_l = Label(frame15, text=pred_y[0], font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)

            col_1_l = Label(frame15, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)

            col_2_l = Label(frame15, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)

            col_3_l = Label(frame15, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
            
            score = Label(frame15, text="Score", font=("Futura", "12", "bold"), bg='light grey',width=12)
            score.place(x=350, y=300)
            
            col_1_en = StringVar()
            col_1_e = Entry(frame15, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)

            col_2_en = StringVar()
            col_2_e = Entry(frame15, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)


            result_btn = Button(frame15, text='Predict', bg='light grey', relief=GROOVE, command=pred_dcr_reg_fn)
            result_btn.place(x=460, y=425)
        def rfr_reg_fn():
            frame2.destroy()

            header_l = Label(win1, text='Random Forest Regression', font=("Futura", "28", "bold"), bg='red', relief=RAISED,
                             padx=6)
            header_l.pack(ipady=10)

            frame16 = Frame(win1, bg='purple')
            frame16.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_rfr_reg_fn():
                
                # Split the data into training and testing sets
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
                
                # Create and train the Random Forest regressor
                regressor = RandomForestRegressor(random_state=0)
                regressor.fit(x_train, y_train)
                
                # Make predictions on the testing set
                y_pred = regressor.predict(x_test)
                
                # Print the predictions for the test set
                print(y_pred)
                
                # Make predictions on new data
                entry1 = col_1_e.get()
                entry2 = col_2_e.get()
                pred_y = regressor.predict([[entry1, entry2]])
                print(pred_y)
                
                # Calculate the R-squared score (coefficient of determination)
                r2 = r2_score(y_test, y_pred)
                print("R-squared Score:", r2)

        
            
                score3 = Label(frame16, text=r2, font=("Futura", "12", "bold"), bg='light grey')
                score3.place(x=600, y=300)

                pred_l = Label(frame16, text=pred_y[0], font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)

            col_1_l = Label(frame16, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)

            col_2_l = Label(frame16, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)

            col_3_l = Label(frame16, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
            
            score = Label(frame16, text="Score", font=("Futura", "12", "bold"), bg='light grey',width=12)
            score.place(x=350, y=300)
            
            col_1_en = StringVar()
            col_1_e = Entry(frame16, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)

            col_2_en = StringVar()
            col_2_e = Entry(frame16, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)


            result_btn = Button(frame16, text='Predict', bg='light grey', relief=GROOVE, command=pred_rfr_reg_fn)
            result_btn.place(x=460, y=425)

        # Classification------------------

        def lcls_fn():
            frame2.destroy()

            header_l = Label(win1, text='Logistic Regression', font=("Futura", "28", "bold"), bg='red', relief=RAISED,
                             padx=6)
            header_l.pack(ipady=10)

            frame8 = Frame(win1, bg='purple')
            frame8.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_logcls_fn():
                # Assuming you have already defined x, y, and col_1_e, col_2_e
                
                # Get user input
                x_entry1 = col_1_e.get()
                x_entry2 = col_2_e.get()
                
                # Standardize the features
                sc = StandardScaler()
                x1 = sc.fit_transform(x)
                x2 = sc.transform([[x_entry1, x_entry2]])  # Use transform instead of fit_transform for user input
                
                # Split the data into training and testing sets
                x_train, x_test, y_train, y_test = train_test_split(x1, y, test_size=0.30, random_state=0)
                
                # Create and train the logistic regression classifier
                classifier = LogisticRegression()
                classifier.fit(x_train, np.ravel(y_train))
                
                # Make predictions on the user input (x2)
                y_pred = classifier.predict(x2)
                
                # Calculate the accuracy score on the testing data
                accuracy = accuracy_score(y_test, classifier.predict(x_test))
                
                acc_lb=accuracy*100

                
                
                
                accuracy_lb = Label(frame8, text=acc_lb, font=("times new roman", "18", "bold"), bg='light grey')
                accuracy_lb.place(x=600, y=300)

                pred_l = Label(frame8, text=y_pred[0], font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)
                # print(pred_y)

            col_1_l = Label(frame8, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)

            accuracy_lb1 = Label(frame8, text='Accuracy', font=("times new roman", "18", "bold"), bg='light grey')
            accuracy_lb1.place(x=350, y=300)

            col_2_l = Label(frame8, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)

            col_3_l = Label(frame8, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)

            col_1_en = StringVar()
            col_1_e = Entry(frame8, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)

            col_2_en = StringVar()
            col_2_e = Entry(frame8, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)

            result_btn = Button(frame8, text='Predict', bg='light grey', relief=GROOVE, command=pred_logcls_fn)
            result_btn.place(x=460, y=375)

        def naive_fn():
            frame2.destroy()

            header_l = Label(win1, text='Naive Bayes', font=("Futura", "28", "bold"), bg='red', relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame9 = Frame(win1, bg='purple')
            frame9.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_nvbys_fn():
                            
                # Split the dataset into a training set and a testing set (e.g., 70% training, 30% testing)
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
                
                # Create and train the Gaussian Naive Bayes classifier
                classifier = GaussianNB()
                classifier.fit(x_train, y_train)
                
                # Make predictions on the testing set
                y_pred = classifier.predict(x_test)
                
                # Calculate the accuracy score
                accuracy = accuracy_score(y_test, y_pred)
                print("Accuracy:", accuracy)
                
                acc_lb=accuracy*100
                
                # Now you can use the classifier to make predictions on new data
                x_entry1 = col_1_e.get()
                x_entry2 = col_2_e.get()
                pred_y = classifier.predict([[x_entry1, x_entry2]])
                print("Predicted Label for New Data:", pred_y)

                accuracy_lb = Label(frame9, text=acc_lb, font=("times new roman", "18", "bold"), bg='light grey')
                accuracy_lb.place(x=600, y=300)
                

                pred_l = Label(frame9, text=pred_y[0], font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)

            col_1_l = Label(frame9, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)
            
            accuracy_lb1 = Label(frame9, text='Accuracy', font=("times new roman", "18", "bold"), bg='light grey')
            accuracy_lb1.place(x=350, y=300)

            col_2_l = Label(frame9, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)

            col_3_l = Label(frame9, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)

            col_1_en = StringVar()
            col_1_e = Entry(frame9, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)

            col_2_en = StringVar()
            col_2_e = Entry(frame9, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)

            result_btn = Button(frame9, text='Predict', bg='light grey', relief=GROOVE, command=pred_nvbys_fn)
            result_btn.place(x=460, y=375)
        def KNN():
            frame2.destroy()

            header_l = Label(win1, text='KNN Algorithm', font=("Futura", "28", "bold"), bg='red', relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame10 = Frame(win1, bg='purple')
            frame10.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_knn():
 

                # Split the dataset into a training set and a testing set (e.g., 70% training, 30% testing)
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
                
                # Standardize the features using StandardScaler
                sc = StandardScaler()
                x_train = sc.fit_transform(x_train)
                x_test = sc.transform(x_test)
                
                # Create and train the K-Nearest Neighbors classifier
                Classifier = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
                Classifier.fit(x_train, y_train)
                
                # Make predictions on the testing set
                y_pred = Classifier.predict(x_test)
                
                # Calculate the accuracy score
                accuracy = accuracy_score(y_test, y_pred)
                print("Accuracy:", accuracy)
                
                acc_lb=accuracy*100
                
                
                # Now you can use the classifier to make predictions on new data
                x_entry1 = col_1_e.get()
                x_entry2 = col_2_e.get()
                # Make sure to preprocess the new data in the same way as the training data
                x_entry = sc.transform([[x_entry1, x_entry2]])
                pred_y = Classifier.predict(x_entry)
                print("Predicted Label for New Data:", pred_y)
                
                accuracy_lb = Label(frame10, text=acc_lb, font=("times new roman", "18", "bold"), bg='light grey')
                accuracy_lb.place(x=600, y=300)
                
                pred_l = Label(frame10, text=y_pred[0], font=("Futura", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)
                
            col_1_l = Label(frame10, text=f'{name_x[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)
            
            accuracy_lb1 = Label(frame10, text='Accuracy', font=("times new roman", "18", "bold"), bg='light grey')
            accuracy_lb1.place(x=350, y=300)

            col_2_l = Label(frame10, text=f'{name_x[1]}', font=("Futura", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)
    
            col_3_l = Label(frame10, text=f'{name_y[0]}', font=("Futura", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
    
            col_1_en = StringVar()
            col_1_e = Entry(frame10, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)
    
            col_2_en = StringVar()
            col_2_e = Entry(frame10, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)

                
            result_btn = Button(frame10, text='Predict', bg='light grey', relief=GROOVE, command=pred_knn)
            result_btn.place(x=460, y=375)
            
            
        def svm_fn():
            frame2.destroy()

            header_l = Label(win1, text='Support Vector Classification', font=("times new roman", "28", "bold"), bg='red', relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame11 = Frame(win1, bg='purple')
            frame11.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_svm():
                x_entry1 = col_1_e.get()
                x_entry2 = col_2_e.get()
                 
                from sklearn.preprocessing import StandardScaler
                sc=StandardScaler()
                # x=sc.fit_transform(x)

                from sklearn.model_selection import train_test_split
                x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)

                from sklearn.svm import SVC
                classifier=SVC(C=1,kernel='rbf',random_state=0,gamma=0.95)
                classifier.fit(x_train,y_train)

                y_pred=classifier.predict(x_test)
                
                a=accuracy_score(y_test, y_pred)
                b=a*100
                print(b)
                
                accuracy_lb = Label(frame11, text=b, font=("times new roman", "18", "bold"), bg='light grey')
                accuracy_lb.place(x=600, y=300)
                
                pred_l = Label(frame11, text=y_pred[0], font=("times new roman", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)
                
            col_1_l = Label(frame11, text=f'{name_x[0]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)
    
            col_2_l = Label(frame11, text=f'{name_x[1]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)
            
            accuracy_lb1 = Label(frame11, text='Accuracy', font=("times new roman", "18", "bold"), bg='light grey')
            accuracy_lb1.place(x=350, y=300)
    
            col_3_l = Label(frame11, text=f'{name_y[0]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
    
            col_1_en = StringVar()
            col_1_e = Entry(frame11, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)
    
            col_2_en = StringVar()
            col_2_e = Entry(frame11, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)

                
            result_btn = Button(frame11, text='Predict', bg='light grey', relief=GROOVE, command=pred_svm)
            result_btn.place(x=460, y=375)   
            
        def dcs_fn():
            frame2.destroy()

            header_l = Label(win1, text='Decision Tree Classification', font=("times new roman", "28", "bold"), bg='red', relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame12 = Frame(win1, bg='purple')
            frame12.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_dcs():
         
                # Split the dataset into a training set and a testing set (e.g., 80% training, 20% testing)
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
                
                # Standardize the features using StandardScaler (if needed)
                sc = StandardScaler()
                # x_train = sc.fit_transform(x_train)
                # x_test = sc.transform(x_test)
                
                # Create and train the Decision Tree classifier
                classifier = DecisionTreeClassifier(random_state=0)
                classifier.fit(x_train, y_train)
                
                # Make predictions on the testing set
                y_pred = classifier.predict(x_test)
                
                # Calculate the accuracy score
                accuracy = accuracy_score(y_test, y_pred)
                accuracy_percentage = accuracy * 100
                print("Accuracy:", accuracy_percentage)
                
                # Now you can use the classifier to make predictions on new data
                x_entry1 = col_1_e.get()
                x_entry2 = col_2_e.get()
                # Make sure to preprocess the new data in the same way as the training data (if needed)
                # x_entry = sc.transform([[x_entry1, x_entry2]])
                
                pred_y = classifier.predict([[x_entry1, x_entry2]])
                print("Predicted Label for New Data:", pred_y)

                accuracy_lb = Label(frame12, text=accuracy_percentage, font=("times new roman", "18", "bold"), bg='light grey')
                accuracy_lb.place(x=600, y=300)
                
                pred_l = Label(frame12, text=y_pred[0], font=("times new roman", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)
                
            col_1_l = Label(frame12, text=f'{name_x[0]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)
    
            col_2_l = Label(frame12, text=f'{name_x[1]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)
            
            accuracy_lb1 = Label(frame12, text='Accuracy', font=("times new roman", "18", "bold"), bg='light grey')
            accuracy_lb1.place(x=350, y=300)
    
            col_3_l = Label(frame12, text=f'{name_y[0]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
    
            col_1_en = StringVar()
            col_1_e = Entry(frame12, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)
    
            col_2_en = StringVar()
            col_2_e = Entry(frame12, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)

                
            result_btn = Button(frame12, text='Predict', bg='light grey', relief=GROOVE, command=pred_dcs)
            result_btn.place(x=460, y=375)    
        def rfc_fn():
            frame2.destroy()

            header_l = Label(win1, text='Random Forest Classification', font=("times new roman", "28", "bold"), bg='red', relief=RAISED, padx=6)
            header_l.pack(ipady=10)

            frame14 = Frame(win1, bg='purple')
            frame14.pack(padx=190, pady=60, ipadx=50, ipady=50, expand=True, fill='both')

            def pred_rfc():
        
                # Split the data into training and testing sets
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
                
                # Standardize the features using StandardScaler (if needed)
                sc = StandardScaler()
                x_train = sc.fit_transform(x_train)
                x_test = sc.transform(x_test)
                
                # Create and train the Random Forest classifier
                classifier = RandomForestClassifier(random_state=0)
                classifier.fit(x_train, y_train)
                
                # Make predictions on the testing set
                y_pred = classifier.predict(x_test)
                
                # Calculate the accuracy score
                accuracy = accuracy_score(y_test, y_pred)
                accuracy_percentage = accuracy * 100
                print("Accuracy:", accuracy_percentage)
                
                # Now you can use the classifier to make predictions on new data
                x_entry1 = col_1_e.get()
                x_entry2 = col_2_e.get()
                # Make sure to preprocess the new data in the same way as the training data (if needed)
                x_entry = sc.transform([[x_entry1, x_entry2]])
                
                pred_y = classifier.predict(x_entry)
                print("Predicted Label for New Data:", pred_y)


                accuracy_lb = Label(frame14, text=accuracy_percentage, font=("times new roman", "18", "bold"), bg='light grey')
                accuracy_lb.place(x=600, y=300)
                
                pred_l = Label(frame14, text=pred_y[0], font=("times new roman", "18", "bold"), bg='light grey')
                pred_l.place(x=600, y=250)
                
            col_1_l = Label(frame14, text=f'{name_x[0]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_1_l.place(x=350, y=150)
    
            col_2_l = Label(frame14, text=f'{name_x[1]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_2_l.place(x=350, y=200)
            
            accuracy_lb1 = Label(frame14, text='Accuracy', font=("times new roman", "18", "bold"), bg='light grey')
            accuracy_lb1.place(x=350, y=300)
    
            col_3_l = Label(frame14, text=f'{name_y[0]}', font=("times new roman", "18", "bold"), bg='light grey')
            col_3_l.place(x=350, y=250)
    
            col_1_en = StringVar()
            col_1_e = Entry(frame14, width=20, textvariable=col_1_en)
            col_1_e.place(x=600, y=150)
    
            col_2_en = StringVar()
            col_2_e = Entry(frame14, width=20, textvariable=col_2_en)
            col_2_e.place(x=600, y=200)

                
            result_btn = Button(frame14, text='Predict', bg='light grey', relief=GROOVE, command=pred_rfc)
            result_btn.place(x=460, y=375)     
        
        # print('algo class',path,"X : ",x_col,"............Y : ",y_col)
        dataset = pd.read_csv(path)
        # print(dataset)
        # print()
        x = dataset.iloc[:, x_col].values
        y = dataset.iloc[:, y_col].values
        # print("x : ",x)
        # print("y : ",y)

        header_l = Label(frame2, text='PREDICTION', font=("Futura", "28", "bold"), bg='red', relief=RAISED, padx=6)
        header_l.pack(ipady=10)

        frame3 = Frame(frame2, bg='#00EE76')
        frame3.pack(fill=BOTH, side=LEFT, expand=True, padx=10, pady=10)

        frame4 = Frame(frame2, bg='#008080')
        frame4.pack(fill=BOTH, side=LEFT, expand=True, padx=10, pady=10)

        #regression buttons-------------------------------

        regression_l = Label(frame3, text='Regression Model', font=("Futura", "22", "bold"), bg='red', relief=RAISED,
                             padx=6)
        regression_l.pack(pady=10)

        lin_reg_btn = Button(frame3, text="Simple-Linear Regression", font=("Futura", "14", "bold"), bg='light grey',
                             relief=GROOVE, command=slin_reg_fn,width=20)
        lin_reg_btn.place(x=200,y=100)

        mul_reg_btn = Button(frame3, text="Multi-Linear Regression", font=("Futura", "14", "bold"), bg='light grey',
                             relief=GROOVE, command=mlin_reg_fn,width=20)
        mul_reg_btn.place(x=200,y=170)

        pol_reg_btn = Button(frame3, text="Polynomial Regression", font=("Futura", "14", "bold"), bg='light grey',
                             relief=GROOVE, command=plin_reg_fn,width=20)
        pol_reg_btn.place(x=200,y=240)

        svr_reg_btn = Button(frame3, text="SVR", font=("Futura", "14", "bold"), bg='light grey',
                             relief=GROOVE, command=svr_reg_fn,width=20)
        svr_reg_btn.place(x=200,y=310)
        
        dcr_reg_btn = Button(frame3, text="Decision Tree", font=("Futura", "14", "bold"), bg='light grey',
                             relief=GROOVE,width=20,command=dcr_reg_fn)
        dcr_reg_btn.place(x=200,y=380)
        
        rfr_reg_btn = Button(frame3, text="Random Forest", font=("Futura", "14", "bold"), bg='light grey',
                             relief=GROOVE,width=20,command=rfr_reg_fn)
        rfr_reg_btn.place(x=200,y=450)
        
        #classification buttons----------------------------------

        classification_l = Label(frame4, text='Classification Model', font=("Futura", "22", "bold"), bg='red',
                                 relief=RAISED, padx=6)
        classification_l.pack(pady=10)

        log_cls = Button(frame4, text="Logistic Regression", font=("Futura", "14", "bold"), bg='light grey',
                         relief=GROOVE, command=lcls_fn,width=20)
        log_cls.place(x=200,y=100)

        nav_bs_btn = Button(frame4, text="Naive - Bayes", font=("Futura", "14", "bold"), bg='light grey', relief=GROOVE,
                            command=naive_fn,width=20)
        nav_bs_btn.place(x=200,y=170)
        
        knn_bs_btn = Button(frame4, text="KNN Algorithm", font=("Futura", "14", "bold"), bg='light grey', relief=GROOVE,width=20,command=KNN)
        knn_bs_btn.place(x=200,y=240)
        
        svc_bs_btn = Button(frame4, text="SVC", font=("Futura", "14", "bold"), bg='light grey', relief=GROOVE,width=20,command=svm_fn)
        svc_bs_btn.place(x=200,y=310)
        
        dt_bs_btn = Button(frame4, text="Decison Tree", font=("Futura", "14", "bold"), bg='light grey', relief=GROOVE,width=20,command=dcs_fn)
        dt_bs_btn.place(x=200,y=380)
        
        rf_bs_btn = Button(frame4, text="Random Forest", font=("Futura", "14", "bold"), bg='light grey', relief=GROOVE,width=20,command=rfc_fn)
        rf_bs_btn.place(x=200,y=450)

        # pol_reg_btn=Button(frame4,text="Polynomial Regression",bg='light grey',relief=RAISED,command=lin_reg_fn)
        # pol_reg_btn.pack(pady=100)

        win1.mainloop()


obb = base()
obb.base_fn()

# = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * = * #