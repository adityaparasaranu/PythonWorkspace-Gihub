"""
This file is for only testing purpose
created by Aditya. This file  name is
test_program.py
"""
from create_table import table
import tkinter as tk

frame = tk.Tk()
frame.title("Test")

t = table.Table(frame, list_of_tuples=[("Car", "Bike", "Bus"), ("Aditya", "Aravind", "Car", "Bike", "Bus")],
                heading=("Test", "Testing", "Lucky", "Aditya"))

frame.mainloop()
