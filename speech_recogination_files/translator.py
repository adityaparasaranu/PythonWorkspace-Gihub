import speech_recognition as sr
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import googletrans
import pyttsx3


frame = tk.Tk()
frame.title("My Translator")
engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

value_list = []

for language in googletrans.LANGUAGES:
    value_list.append(googletrans.LANGUAGES.get(language))

text_to_be_translated = tk.StringVar()
selected_lang = tk.StringVar()

info = tk.Label(frame, text="Type the text below which have to be translated", fg="red").grid(row=0, column=0)
text_area = tk.Entry(frame,width=45, highlightbackground="black", textvariable=text_to_be_translated).grid(row=2, column=0)

info_2 = tk.Label(frame, text="Select a language for the above text to be translated", fg="red").grid(row=5, column=0)
available_lang = ttk.Combobox(frame, textvariable=selected_lang, values=value_list, state="readonly").grid(row=6, column=0)


def speech_function():
    messagebox.showinfo("Information", "This can only record and understand english language. So speak in english")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print(r.recognize_google(audio))
    text_area.insert(0, r.recognize_google(audio))


speech_button = tk.Button(frame, text="Speech Recognition", fg="blue", command=speech_function).grid(row=2, column=1)


def translate_function():
    translator = googletrans.Translator()
    translations = translator.translate(text_to_be_translated.get(), dest=selected_lang.get()).text
    label = tk.Label(frame, text="The below is your translated sentence", fg="red").grid(row=1, column=4)
    translated_text_label = tk.Label(frame, text=translations).grid(row=2, column=4)


translate_button = tk.Button(frame, text="Translate", fg="blue", command=translate_function).grid(row=7, column=1)

frame.mainloop()
