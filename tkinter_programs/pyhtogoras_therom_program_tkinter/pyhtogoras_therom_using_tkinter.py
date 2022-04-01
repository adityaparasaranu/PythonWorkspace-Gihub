from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import math

frame = tk.Tk()
frame.title("Pyhtogoras Therom App")

a_side = tk.StringVar()
b_side = tk.StringVar()
c_side = tk.StringVar()


def action():
    string_vars = a_side.get(), b_side.get(), c_side.get()

    count = 0

    for var in string_vars:
        if var == "" or var == str:
            messagebox.showerror("Error", "You have not given the right value in some places. So Please try agian")
            quit()

        elif var == "To Be Found":
            count += 1

    if count >= 2:
        messagebox.showerror('Error', 'You have given "To Be Found" option for more than 1 time. So Please try again')

    elif count == 0:
        messagebox.showerror('Error', 'You have not given "To Be Found" option at all. So Please try again')

    try:
        if a_side.get() == "To Be Found":
            num = int(c_side.get())**2 - int(b_side.get()) ** 2
            final_answer = math.sqrt(num)

            messagebox.showinfo('Answer', f'The Answer is "{final_answer:3f}"')

        elif b_side.get() == "To Be Found":
            num = int(c_side.get()) ** 2 - int(a_side.get()) ** 2
            final_answer = math.sqrt(num)

            messagebox.showinfo('Answer', f'The Answer is "{final_answer:3f}"')

        elif c_side.get() == "To Be Found":
            num = int(a_side.get()) ** 2 + int(b_side.get()) ** 2
            final_answer = math.sqrt(num)

            messagebox.showinfo('Answer', f'The Answer is "{final_answer:3f}"')
    except ValueError:
        messagebox.showerror("Error", "You have not given the right value in some places. So Please try agian")


welcome_label = tk.Label(frame, text= "Welcome to Pyhtogoras Therom App !", fg= "red").grid(row= 0, column=0)
info_label = tk.Label(frame, text= 'Type the length of any 2 sides and select', fg= "green").grid(row= 2, column=0)
info_label_2 = tk.Label(frame, text= '"To Be Found"option if it is to be found', fg= "green").grid(row= 3, column=0)

a_label = tk.Label(frame, text= '"a" side length : ').grid(row= 4, column=0)
a_entry = ttk.Combobox(frame, textvariable=a_side, values=["To Be Found"]).grid(row=4, column=1)

b_label = tk.Label(frame, text= '"b" side length : ').grid(row= 5, column=0)
b_entry = ttk.Combobox(frame, textvariable=b_side, values=["To Be Found"]).grid(row=5, column=1)

c_label = tk.Label(frame, text= '"c" side length : ').grid(row= 6, column=0)
c_entry = ttk.Combobox(frame, textvariable=c_side, values=["To Be Found"]).grid(row=6, column=1)

find_button = tk.Button(frame, text= "Find the Result", fg= "blue", command= action).grid(row= 7, column= 0)
exit_button = tk.Button(frame, text= "Exit", fg= "magenta", command= frame.destroy).grid(row= 7, column= 1)

frame.mainloop()
