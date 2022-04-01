import os

import playsound
import speech_recognition as sr
from gtts import gTTS
import googletrans

r = sr.Recognizer()
mic = sr.Microphone()
translator = googletrans.Translator()

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)

print("Processing the audio...")
try:
    print(f"What you spoke : {r.recognize_google(audio)}")
except sr.UnknownValueError:
    print("Nothing was listened")
    quit()

text = r.recognize_google(audio)
translations = translator.translate(text, dest="tamil").text
print(f"Translated text : {translations}")


def tamil_speech_function(tamil_text):
    tts = gTTS(text=tamil_text, lang="ta")
    tts.save("tamil_audio.mp3")
    playsound.playsound("tamil_audio.mp3")
    os.remove("tamil_audio.mp3")


tamil_speech_function(translations)
