from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import tkinter as tk
import sqlite3
import random

frame = tk.Tk()

account_numbers = ["123 452 672 976", "456 787 876 086", "679 798 998 757", "767 978 673 133", "268 298 367 673",
                   "454 786 779 976", "878 878 656 778", "123 465 987 078",
                   "446 873 982 037", "275 972 872 800", "284 029 289 972"]

frame.title("ARADI Bank")

finding_email_var = tk.StringVar()
finding_password_entry = tk.StringVar()

name_var = tk.StringVar()
gender_var = tk.StringVar()
age_var = tk.StringVar()
occupation_var = tk.StringVar()
email_id_var = tk.StringVar()
country_var = tk.StringVar()
state_var = tk.StringVar()
city_var = tk.StringVar()
address_var = tk.StringVar()
phone_no_var = tk.StringVar()
set_password_var = tk.StringVar()

welcome = tk.Label(frame, text="Welcome to ARADI Bank", fg="red").grid(row=0, column=0)
welcome_2 = tk.Label(frame, text="Register the below details to be a member of ARADI Bank", fg="red").grid(row=1,
                                                                                                           column=0)

name_label = tk.Label(frame, text="Name").grid(row=2, column=0)
name = tk.Entry(frame, textvariable=name_var).grid(row=2, column=1)

gender_label = tk.Label(frame, text= "Gender").grid(row= 3, column= 0)
gender = ttk.Combobox(frame, textvariable= gender_var, values= ["Male", "Female"], state= "readonly").grid(row= 3, column= 1)

age_label = tk.Label(frame, text="Age").grid(row=4, column=0)
age = tk.Entry(frame, textvariable=age_var).grid(row=4, column=1)

occupation_label = tk.Label(frame, text="Occupation").grid(row=5, column=0)
occupation = tk.Entry(frame, textvariable=occupation_var).grid(row=5, column=1)

important = tk.Label(frame, text="(Make Sure that the Email - Id you are giving is not used by another person!)", fg="red").grid(row=6, column=0)

email_id_label = tk.Label(frame, text="Email Id").grid(row=7, column=0)
email_id = tk.Entry(frame, textvariable=email_id_var).grid(row=7, column=1)

country_label = tk.Label(frame, text="Country").grid(row=8, column=0)
country = ttk.Combobox(frame, textvariable= country_var, values= ["India"], state= "readonly").grid(row= 8, column= 1)

state_label = tk.Label(frame, text="State").grid(row=9, column=0)
state = ttk.Combobox(frame, textvariable=state_var, values= ["Tamil Nadu", "Andhra Pradesh", "Assam", "Arunachal Pradesh", "Bihar", "Goa", "Gujarat", "Jammu and Kashmir", "Jharkhand", "West Bengal", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Punjab", "Rajasthan", "Sikkim", "Tripura", "Uttaranchal", "Uttar Pradesh", "Haryana", "Himachal Pradesh", "Chhattisgarh"], state= "readonly").grid(row=9, column=1)

city_label = tk.Label(frame, text="City").grid(row=10, column=0)
city = tk.Entry(frame, textvariable=city_var).grid(row=10, column=1)

address_label = tk.Label(frame, text="Address").grid(row=11, column=0)
address = tk.Entry(frame, textvariable=address_var).grid(row=11, column=1)

phone_no_label = tk.Label(frame, text="Phone Number").grid(row=12, column=0)
phone_no = tk.Entry(frame, textvariable=phone_no_var).grid(row=12, column=1)

set_password_label = tk.Label(frame, text="Set Password").grid(row=13, column=0)
set_password_entry = tk.Entry(frame, show="•", textvariable=set_password_var).grid(row=13, column=1)


def create_table():
    random_account_number = random.choice(account_numbers)
    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()

    cursor.execute("SELECT email FROM customers_details WHERE email= ?", (email_id_var.get().strip().lower(),))
    same_email_id = cursor.fetchall()

    if len(same_email_id) == 0:
        cursor.execute("INSERT INTO customers_details VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
            name_var.get().strip().lower().title(), gender_var.get(), age_var.get(), occupation_var.get(),
            email_id_var.get().strip().lower(),
            country_var.get(), state_var.get(), city_var.get(), address_var.get(), phone_no_var.get(),
            random_account_number, set_password_var.get(),))

        messagebox.showinfo("Thank You",
                            f"Your request is submitted successfully {name_var.get().strip().lower().title()} !")

    elif len(same_email_id) != 0:
        messagebox.showerror("Error", "This Email Id has been given by another person! Pls try again")

    connection.commit()
    connection.close()
    quit()


def try_catch_function():
    random_account_number = random.choice(account_numbers)

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE customers_details(name text, gender text, age text, occupation text, email text, country text, state text, city text, address text, phone_no text, account_number integer, set_password text)")
    except sqlite3.OperationalError:
        connection.commit()
        connection.close()

        create_table()
    else:
        cursor.execute("INSERT INTO customers_details VALUES(?,? ,?,?,?,?,?,?,?,?,?,?)", (
            name_var.get().strip().lower().title(), gender_var.get(), age_var.get(), occupation_var.get(),
            email_id_var.get().strip().lower(),
            country_var.get(), state_var.get(), city_var.get(), address_var.get(), phone_no_var.get(),
            random_account_number,
            set_password_var.get()), )

        connection.commit()
        connection.close()

        messagebox.showinfo("Thank You",
                            f"Your request is submitted successfully {name_var.get().strip().lower().title()} !")
        quit()

    connection.commit()
    connection.close()


def action():
    # The below `if` and `elif` statements are to check whether the values are proper
    # Checking the name value below
    if name_var.get().isspace() or name_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking the age value
    elif age_var.get().isnumeric() == False:
        messagebox.showerror("Error",
                             f"Sorry you are not eligible with this age {name_var.get().strip().lower().title()}!. Pls try again")
        quit()

    # Checking the occupation value
    elif occupation_var.get().isspace() or occupation_var.get() == "" or occupation_var.get().isnumeric():
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking Email Id Value
    wrong_email_id = True
    for letter in email_id_var.get():
        if letter == "@":
            wrong_email_id = False
    if wrong_email_id == True:
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking Country Value
    elif country_var.get().isspace() or country_var.get().isnumeric() or country_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking State Value
    elif state_var.get().isspace() or state_var.get().isnumeric() or state_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking City Value
    elif city_var.get().isspace() or city_var.get().isnumeric() or city_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking Address Value
    elif address_var.get().isspace() or address_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking Phone Number Vaue
    elif phone_no_var.get().isnumeric() == False or phone_no_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking the Password Value
    elif set_password_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    try_catch_function()


submit = tk.Button(frame, text="Submit", fg="blue", command=action).grid(row=14, column=0)

find_label = tk.Label(frame, text="If you are a ARADI Bank customer and want to ", fg="red").grid(row=2, column=13)
find_label_2 = tk.Label(frame, text="know your details enter your Email and Password below", fg="red").grid(row=3, column=13)


email_label = tk.Label(frame, text="Email").grid(row=4, column=12)
email_entry = tk.Entry(frame, textvariable=finding_email_var).grid(row=4, column=13)

password_label = tk.Label(frame, text="Password").grid(row=5, column=12)
password_entry = tk.Entry(frame, show="•", textvariable=finding_password_entry).grid(row=5, column=13)


def finding_customers():
    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()
    cursor.execute(
        "SELECT name, gender, age, occupation, email, country, state, city, address, phone_no, account_number FROM customers_details WHERE email= ? AND set_password= ?",
        (finding_email_var.get().strip().lower(), finding_password_entry.get(),))

    customer_detail = []

    for tuples in cursor.fetchall():
        for i in tuples:
            customer_detail.append(i)

    if len(customer_detail) != 0:
        printing_details = f"""Name : {customer_detail[0]}
Gender        : {customer_detail[1]}
Age : {customer_detail[2]}
Occupation   : {customer_detail[3]}
Email Id    : {customer_detail[4]}
Country      : {customer_detail[5]}
State       : {customer_detail[6]}
City    : {customer_detail[7]}
Address  : {customer_detail[8]}
Phone No : {customer_detail[9]}
Account Number : {customer_detail[10]}
"""
        messagebox.showinfo("Your Details", f"{printing_details}")
        quit()

    elif len(customer_detail) == 0:
        messagebox.showerror("Error",
                             "There is no such Registerd Details with the Email Id you have given. Pls try again")
        quit()


find_button = tk.Button(frame, text="Find", fg="blue", command=finding_customers).grid(row=6, column=13)


# Inserting the sign in buttons and other stuffs


def sign_in_function():
    user_name = simpledialog.askstring("Sign In", "User Name")
    sign_in_password = simpledialog.askstring("Sign In", "Password", show="•")

    if user_name == "aditya@gmail.com" and sign_in_password == "aditya":
        messagebox.showinfo("Success", "You have signed in successfully !")

        frame.destroy()
        frame.quit()

        root = Tk()
        try:
            connection = sqlite3.connect("database.db")

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM customers_details")

            customers = cursor.fetchall()
            customers.insert(0, ("Name", "Gender", "Age", "Occupation", "Email Id", "Country", "State", "City", "Address", "Phone No", "Account No", "Password"))

            connection.commit()
            connection.close()

        except sqlite3.OperationalError:
            messagebox.showinfo("Information", "There is no ARADI Bank customers till now. Pls try again")
            quit()

        else:
            class Table:
                def __init__(self, root):

                    total_rows = len(customers)
                    total_columns = len(customers[0])
                    flag = 0

                    if len(customers) == 1:
                        messagebox.CANCEL(frame)

                    for i in range(total_rows):
                        for j in range(total_columns):
                            if flag == 0:
                                self.e = Entry(root, width=10, fg='red', font= ("Arial", 13, "bold"))
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, customers[i][j])

                                if j == 11:
                                    flag = flag + 1

                            else:
                                self.e = Entry(root, width=10, fg='blue')
                                self.e.grid(row=i, column=j)
                                self.e.insert(END, customers[i][j])

            table = Table(root)

            root.title("ARADI Bank Customers")
            root.mainloop()

    else:
        messagebox.showerror("Error", f'You have entered the "User Name" or "Password" wrongly ! Pls try again')


sign_in_label = tk.Label(frame, text='Caution ! The below "Sign In" Button is only for higher officials. Do not use '
                                     'it unnecessarily !', fg="red").grid(row=15, column=13)
sign_in_button = tk.Button(frame, text="Sign In", fg="blue", command=sign_in_function).grid(row=16, column=13)


def exit_question():
    msg = tk.messagebox.askquestion("Are you Sure?", "Are you sure, you want to exit ARADI Bank ?", icon= "warning")

    if msg == "yes":
        frame.destroy()


exit_button = tk.Button(frame, text= "Exit", fg= "green", command= exit_question).grid(row= 16, column= 0)
frame.mainloop()
