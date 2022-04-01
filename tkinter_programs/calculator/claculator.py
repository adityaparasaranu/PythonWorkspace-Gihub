import tkinter as tk

frame = tk.Tk()
frame.title("Calculator")
frame.geometry("180x180")


class Actions:
    def __init__(self):
        self.calculation = tk.StringVar()
        self.display = tk.Label(frame, text=self.calculation).grid(row=0, column=0)

    def action_for_1(self):
        calc = self.calculation.get()
        calc += '1'
        self.calculation.set(calc)

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass

    def action_for_1(self):
        pass


action_obj = Actions()

one = tk.Button(frame, text= "    1    ", command=action_obj.action_for_1).grid(row= 1, column= 1)
# two = tk.Button(frame, text= "    2    ", command=action).grid(row= 1, column= 2)
# three = tk.Button(frame, text= "    3    ", command=action).grid(row= 1, column= 3)
#
# four = tk.Button(frame, text= "    4    ", command= action).grid(row= 2, column= 1)
# five = tk.Button(frame, text= "    5    ", command= action).grid(row= 2, column= 2)
# six = tk.Button(frame, text= "    6    ", command= action).grid(row= 2, column= 3)
#
# seven = tk.Button(frame, text= "    7    ", command=action).grid(row= 3, column= 1)
# eight = tk.Button(frame, text= "    8    ", command=action).grid(row= 3, column= 2)
# nine = tk.Button(frame, text= "    9    ", command=action).grid(row= 3, column= 3)
#
# plus_sign = tk.Button(frame, text= "    +    ", command=action).grid(row= 1, column= 4)
# minus_sign = tk.Button(frame, text= "    -    ", command=action).grid(row= 2, column= 4)
# multiply_sign = tk.Button(frame, text= "    x    ", command=action).grid(row= 3, column= 4)
# divison_sign = tk.Button(frame, text= "    ÷    ", command=action).grid(row= 4, column= 4)
#
# equals = tk.Button(frame, text= "    =    ", command=action).grid(row= 4, column= 1)

frame.mainloop()
