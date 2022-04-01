from tkinter import messagebox
import tkinter as tk
import random

frame = tk.Tk()

account_numbers = ["123 452 672 976", "456 787 876 086", "679 798 998 757", "767 978 673 133", "268 298 367 673", "454 786 779 976 989", "878 878 656 778"]

frame.title("ARADI Bank")

name_var = tk.StringVar()
age_var = tk.StringVar()
occupation_var = tk.StringVar()
country_var = tk.StringVar()
state_var = tk.StringVar()
city_var = tk.StringVar()
address_var = tk.StringVar()
phone_no_var = tk.StringVar()
password_var = tk.StringVar()

welcome = tk.Label(frame, text= "Welcome to ARADI Bank", fg= "red").grid(row= 0, column= 0)
welcome_2 = tk.Label(frame, text= "Register the below details to be a member of ARADI Bank", fg= "red").grid(row= 1, column= 0)

name_label = tk.Label(frame, text= "Name").grid(row= 2, column= 0)
name = tk.Entry(frame, textvariable= name_var).grid(row= 2, column= 1 )

age_label = tk.Label(frame, text= "Age").grid(row= 3, column= 0)
age = tk.Entry(frame, textvariable= age_var).grid(row= 3, column= 1)

occupation_label = tk.Label(frame, text= "Occupation").grid(row= 4, column= 0)
occupation = tk.Entry(frame, textvariable= occupation_var).grid(row= 4, column= 1)

country_label = tk.Label(frame, text= "Country").grid(row= 5, column= 0)
country = tk.Entry(frame, textvariable= country_var).grid(row= 5, column= 1)

state_label = tk.Label(frame, text= "State").grid(row= 6, column= 0)
state = tk.Entry(frame, textvariable= state_var).grid(row= 6, column= 1)

city_label = tk.Label(frame, text= "City").grid(row= 7, column= 0)
city = tk.Entry(frame, textvariable= city_var).grid(row= 7, column= 1)

address_label = tk.Label(frame, text= "Address").grid(row= 8, column= 0)
address = tk.Entry(frame, textvariable= address_var).grid(row= 8, column= 1)

phone_no_label = tk.Label(frame, text= "Phone Number").grid(row= 9, column= 0)
phone_no = tk.Entry(frame, textvariable= phone_no_var).grid(row= 9, column= 1)

password_label = tk.Label(frame, text= "Set Password").grid(row= 10, column= 0)
password = tk.Entry(frame, show= "*", textvariable= password_var).grid(row= 10, column= 1)

def action() :
    account_number = random.choice(account_numbers)
    messagebox.showinfo("ARADI Bank", f'''Hi {name_var.get()}. You have successfully created an account in ARADI Bank!,
Your account number is : {account_number}
Your password is "{password_var.get()}"
You are working as {occupation_var.get()}.
Your phone number is {phone_no_var.get()}, and you are located in
{country_var.get()}, {state_var.get()}, {city_var.get()}, {address_var.get()}.
Your age is {age_var.get()}.


Thank You 🙏 for creating a account in ARADI Bank , {name_var.get()}
''')
    quit()

submit = tk.Button(frame, text= "Submit", fg="blue", command= action).grid(row= 11, column= 0)

frame.mainloop()
