import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

troly=pyttsx3.init()
voice=troly.getProperty('voices')
troly.setProperty('voice',voice[1].id)

def speak(audio):
    print('Trợ lý ảo: ' + audio)
    troly.say(audio)
    troly.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I: %M: %p")
    speak("The current time is")
    print(Time)
    troly.say(Time)
    troly.runAndWait()

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good morning sir")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("How can i help you")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("ông chủ: " + query)
    except sr.UnknownValueError:
        print("Ông chủ thử nói lại hoặc gõ lệnh tay nha")
        query=str(input('lệnh của ông chủ: '))
    return query

if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should i search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak("What should i search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open image" in query:
            meme=r"C:\Users\Tuan\Downloads\Dual-Monitor-Wallpaper-4.jpg"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Goodbye boss")
            quit()
            