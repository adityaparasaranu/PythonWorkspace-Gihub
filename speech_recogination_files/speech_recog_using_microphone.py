import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()
# print(mic.list_microphone_names())

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)

print("Processing the audio...")
try:
    print(r.recognize_google(audio))
    engine.say(r.recognize_google(audio))
    engine.runAndWait()
except sr.UnknownValueError:
    print("Nothing was listened")


