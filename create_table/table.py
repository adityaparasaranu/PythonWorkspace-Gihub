"""
This file is created to put the list of tuples
data, into a table using tkinter entry's.
We can import this anywhere and use it
to create a table
"""
from tkinter import *


class Table:
    def __init__(self, frame: Tk, list_of_tuples: list, heading: tuple = None):
        flag = 0

        if heading is not None:
            list_of_tuples.insert(0, heading)

        for i in range(len(list_of_tuples)):
            for j in range(len(list_of_tuples[i])):

                if heading is not None and flag == 0:

                    self.e = Entry(frame, width=10, fg='red', font=("Arial", 13, "bold"))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, list_of_tuples[i][j])

                    if j == len(list_of_tuples[0]) - 1:
                        flag = flag + 1

                else:
                    self.e = Entry(frame, width=10, fg='blue')
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, list_of_tuples[i][j])
