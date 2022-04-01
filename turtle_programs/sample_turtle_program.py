import tkinter as tk
import turtle

my_turtle = turtle.Turtle()

frame = tk.Tk()

def drawing():
    fd = 50
    for _ in range(100):
        my_turtle.forward(fd)
        my_turtle.right(90)
        fd += 10


def circle():
    turtle.circle(2)


circle = tk.Button(frame, text= "Circle", command= circle).grid(row= 0, column= 1)
rec = tk.Button(frame, text= "Rectangle", command= drawing).grid(row= 0, column= 2)



turtle.done()
