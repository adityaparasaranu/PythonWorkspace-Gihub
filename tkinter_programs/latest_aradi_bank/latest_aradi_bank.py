from tkinter import messagebox
import tkinter as tk
import random

frame = tk.Tk()

account_numbers = ["123 452 672 976", "456 787 876 086", "679 798 998 757", "767 978 673 133", "268 298 367 673", "454 786 779 976", "878 878 656 778", "123 465 987 078",
                   "446 873 982 037", "275 972 872 800", "284 029 289 972"]

frame.title("ARADI Bank")

finiding_email_var = tk.StringVar()
finding_password_entry = tk.StringVar()

name_var = tk.StringVar()
age_var = tk.StringVar()
occupation_var = tk.StringVar()
email_id_var = tk.StringVar()
country_var = tk.StringVar()
state_var = tk.StringVar()
city_var = tk.StringVar()
address_var = tk.StringVar()
phone_no_var = tk.StringVar()
set_password_var = tk.StringVar()

welcome = tk.Label(frame, text= "Welcome to ARADI Bank", fg= "red").grid(row= 0, column= 0)
welcome_2 = tk.Label(frame, text= "Register the below details without commas to be a member of ARADI Bank", fg= "red").grid(row= 1, column= 0)

name_label = tk.Label(frame, text= "Name").grid(row= 2, column= 0)
name = tk.Entry(frame, textvariable= name_var).grid(row= 2, column= 1 )

age_label = tk.Label(frame, text= "Age").grid(row= 3, column= 0)
age = tk.Entry(frame, textvariable= age_var).grid(row= 3, column= 1)

occupation_label = tk.Label(frame, text= "Occupation").grid(row= 4, column= 0)
occupation = tk.Entry(frame, textvariable= occupation_var).grid(row= 4, column= 1)

important = tk.Label(frame, text= "(Make Sure that the Email - Id you are giving is not used by another person!)", fg= "red").grid(row= 5, column= 0)

email_id_label = tk.Label(frame, text= "Email Id").grid(row= 6, column= 0)
email_id = tk.Entry(frame, textvariable= email_id_var).grid(row= 6, column= 1)

country_label = tk.Label(frame, text= "Country").grid(row= 7, column= 0)
country = tk.Entry(frame, textvariable= country_var).grid(row= 7, column= 1)

state_label = tk.Label(frame, text= "State").grid(row= 8, column= 0)
state = tk.Entry(frame, textvariable= state_var).grid(row= 8, column= 1)

city_label = tk.Label(frame, text= "City").grid(row= 9, column= 0)
city = tk.Entry(frame, textvariable= city_var).grid(row= 9, column= 1)

address_label = tk.Label(frame, text= "Address").grid(row= 10, column= 0)
address = tk.Entry(frame, textvariable= address_var).grid(row= 10, column= 1)

phone_no_label = tk.Label(frame, text= "Phone Number").grid(row= 11, column= 0)
phone_no = tk.Entry(frame, textvariable= phone_no_var).grid(row= 11, column= 1)

set_password_label = tk.Label(frame, text="Set Password").grid(row= 12, column= 0)
set_password_entry = tk.Entry(frame, show="*", textvariable= set_password_var).grid(row= 12, column= 1)


def action():
    with open("aradi_bank_details.txt", "r") as aradi_bank_file:
        list_of_contents = aradi_bank_file.readlines()
    flag = False
    random_account_number = random.choice(account_numbers)

# The below `if` and `elif` statements are to check whether the values are proper
    # Checking the name value below
    if name_var.get().isspace() or name_var.get() == "":
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
        quit()

    # Checking the age value
    elif age_var.get().isnumeric() == False:
        messagebox.showerror("Error", "You have give a wrong value or not give value in some places. Pls try again")
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
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------


# The below `if` and `elif` statements are to check whether the email give is same as the email given by another person
    if len(list_of_contents) == 0:
        with open("aradi_bank_details.txt", "a") as aradi_bank_file:
            aradi_bank_file.writelines(f"{name_var.get()},{age_var.get()},{occupation_var.get()},{email_id_var.get().strip().lower()},{country_var.get()},{state_var.get()},{city_var.get()},{address_var.get()},{phone_no_var.get()},{random_account_number},{set_password_var.get()}")
            aradi_bank_file.writelines("\n")
        messagebox.showinfo("Thank You", f"Your response was submitted successfully {name_var.get().strip()}! Your account number is {random_account_number}")
        quit()

    elif len(list_of_contents) != 0:
        for lists in list_of_contents:
            customers_details = lists.strip().split(',')
            if customers_details[3] == email_id_var.get().strip().lower():
                flag = True

        if flag == False:
            with open("aradi_bank_details.txt", "a") as aradi_bank_file:
                aradi_bank_file.writelines(f"{name_var.get()},{age_var.get()},{occupation_var.get()},{email_id_var.get().strip().lower()},{country_var.get()},{state_var.get()},{city_var.get()},{address_var.get()},{phone_no_var.get()},{random_account_number},{set_password_var.get()}")
                aradi_bank_file.writelines("\n")
            messagebox.showinfo("Thank You", f"Your response was submitted successfully {name_var.get().strip()}! Your account number is {random_account_number}")
            quit()

        elif flag == True:
            messagebox.showerror("Error", "The Email Id you have given is given by another person! Pls try again")
            quit()


submit = tk.Button(frame, text= "Submit", fg="blue", command= action).grid(row= 13, column= 0)

find_label = tk.Label(frame, text= "If you are a ARADI Bank customer and want to ", fg= "red").grid(row= 2, column= 13)
find_label_2 = tk.Label(frame, text= "know your details enter your Email and Password below", fg= "red").grid(row=3, column= 13)

email_label = tk.Label(frame, text= "Email").grid(row= 4, column= 12)
email_entry = tk.Entry(frame, textvariable= finiding_email_var).grid(row=4, column= 13)

password_label = tk.Label(frame, text= "Password").grid(row= 5, column= 12)
password_entry = tk.Entry(frame, show="*", textvariable= finding_password_entry).grid(row= 5, column= 13)


def finding():
    with open("aradi_bank_details.txt", "r") as aradi_bank_file:
        list_of_contents = aradi_bank_file.readlines()

    if len(list_of_contents) == 0:
        messagebox.showerror("Error", "The Email Id or Password you have given maybe wrong! Pls try again")
        quit()

    elif len(list_of_contents) != 0:
        for lists in list_of_contents:
            customer_details = lists.strip().split(',')
            printing_details = f"""Hi {customer_details[0]}. Your Details are below
Name       : {customer_details[0]}
Age        : {customer_details[1]}
Occupation : {customer_details[2]}
Email Id   : {customer_details[3]}
Country    : {customer_details[4]}
State      : {customer_details[5]}
City       : {customer_details[6]}
Address    : {customer_details[7]}
Phone Number   : {customer_details[8]}
Account Number : {customer_details[9]}"""
            if customer_details[3] == finiding_email_var.get().strip().lower() and customer_details[-1] == finding_password_entry.get():
                messagebox.showinfo(f"{customer_details[0]} Details", f"{printing_details}")
                quit()


find_button = tk.Button(frame, text= "Find", fg= "blue", command= action).grid(row=6, column=13)

frame.mainloop()
