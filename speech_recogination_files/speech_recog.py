import speech_recognition as sr

r = sr.Recognizer()
file = sr.AudioFile("test.wav")

with file as source:
    audio = r.record(source, offset=4, duration=3.2)

print(r.recognize_google(audio))