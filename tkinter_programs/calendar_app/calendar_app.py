import calendar
import tkinter as tk

frame = tk.Tk()
frame.title("Calendar App")

year = tk.StringVar()


def action():
    root = tk.Tk()

    root.config(background="white")
    root.title("Calendar")
    root.geometry("550x600")

    fetch_year = int(year.get())

    calendar_content = calendar.calendar(fetch_year)
    calendar_label = tk.Label(root, text=calendar_content, font= "Consolas 10 bold").grid(row= 5, column= 1, padx= 30)

    root.mainloop()


info_label = tk.Label(frame, text= "Enter a year below to see the calendar for that year", fg= "red").grid(row= 0, column= 0)

year_label = tk.Label(frame, text= "Year").grid(row= 1, column= 0)
year_entry = tk.Entry(frame, textvariable=year).grid(row= 1, column= 1)

show_calendar_button = tk.Button(frame, text= "Show Calendar", command= action, fg= "blue").grid(row= 2, column= 0)

frame.mainloop()
