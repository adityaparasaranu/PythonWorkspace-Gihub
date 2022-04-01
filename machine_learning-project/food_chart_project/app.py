import joblib
import warnings
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')
model = joblib.load("food_model.joblib")

frame = tk.Tk()
frame.title("User Form")
frame.geometry("500x300+370+200")

age = tk.StringVar()
gender = tk.StringVar()
occupation = tk.StringVar()


def pie_chart_func(prediction):
    plt.title("Food Chart")
    plt.rcParams['toolbar'] = 'None'
    labels = ["Carbohydrate", "Proteins", "Fats", "Vitamins and Minerals"]
    prediction_list = list(prediction)[0]
    plt.pie(prediction_list, labels=labels, wedgeprops={"edgecolor": "black"}, autopct="%1.1f%%")
    plt.show()

    age.set("")
    gender.set("")
    occupation.set("")


def prediction_func():
    global user_gender
    try:
        int(age.get())
    except:
        messagebox.showerror("Error", 'You have given wrong or invalid value in place of "Age"')
        age.set("")
        return
    user_occupation = occupation.get()
    user_age = int(age.get())

    if user_age < 18 and user_occupation != "Student":
        messagebox.showerror("Error", 'Your age is below 18 years and you have selected option other than '
                                      '"Student" option. Pls select the Student option')
        age.set("")
        gender.set("")
        occupation.set("")
        return

    if gender.get() == "Male":
        user_gender = 1
    elif gender.get() == "Female":
        user_gender = 0

    occupation_dict = dict(zip(occupation_list, occupation_integers))
    prediction = model.predict( [ [user_age, user_gender, occupation_dict.get(user_occupation) ] ] )

    pie_chart_func(prediction)


info_label = tk.Label(frame, text='Enter the below details to see your food chart', fg="green", pady=20,
                      font=("Helvetica", 20)).grid(row=0, columnspan=2)

age_label = tk.Label(frame, text='Age', pady=10, font=("Helvetica", 15)).grid(row=2, column=0)
age_entry = tk.Entry(frame, textvariable=age, borderwidth=3).grid(row=2, column=1)

gender_label = tk.Label(frame, text='Gender', pady=10, font=("Helvetica", 15)).grid(row=3, column=0)
gender_entry = ttk.Combobox(frame, textvariable=gender, values=["Male", "Female"], state="readonly", width=18).grid(row=3, column=1)

occupation_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
occupation_list = ["Software engineer", "Student", "Constructional worker", "Teacher", "Hospital workers", "Housekeeping",
                   "Delivery persons", "White-collar", "Police"]
occupation_label = tk.Label(frame, text='Occupation', pady=5, font=("Helvetica", 15)).grid(row=4, column=0)
occupation_entry = ttk.Combobox(frame, textvariable=occupation, values=occupation_list, state="readonly", width=18).grid(row=4,
                                                                                                               column=1)

submit_button = tk.Button(frame, text="Submit", fg="blue", command=prediction_func, pady=5, padx=5).grid(row=5, column=1)

frame.mainloop()
