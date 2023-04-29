# pip install pyaudio

# pip install pyttsx3
import pyttsx3
# pip install speechRecognition
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import wikipedia as wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir, please tell me hoe may i help ypu")


def takeCommand():
    # It takes microphone input from the user abd returns string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'your_password')
    server.sendmail('yourmail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    WishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("serching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow")
        elif 'play music' in query:
            music_dir = 'F:\HipHop Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codepath = r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'emial to Tejas' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "tejasdf.77@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend, I am not able to send this email!")
        else:
            print("No query Matched!")
