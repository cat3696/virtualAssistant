import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak('Now listening')
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-US')
            print("The command is printed = ", query)
        except Exception as e:
            print(e)
            speak("Please say that one more time")
            return "None"
        return query


def hello():
    speak("Hello there! I am your desktop buddy. "
          "For a list of available commands, ask what can you do")


def take_query():
    hello()

    while True:
        query = take_command().lower()
        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "what day is it" in query:
            day = datetime.datetime.today().weekday() + 1

            day_dict = {1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}

            if day in day_dict.keys():
                day_of_the_week = day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)
            continue

        elif "what time is it" in query:
            time = str(datetime.datetime.now())
            print(time[11:16])
            hour = time[11:13]
            minute = time[14:16]
            speak("In military time, it is currently " + hour + minute)
            continue

        elif "thank you stop" in query:
            speak("Until next time")
            exit()

        elif "open microsoft word" in query:
            speak("Opening Microsoft Word")
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
            continue

        elif "open google chrome" in query:
            speak("Google Chrome")
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            continue

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(result)
            continue

        elif "tell me your name" in query:
            speak("I am Penelope! Your virtual Assistant")
            continue

        elif "what can you do" in query:
            speak("if you say open site name I can open a website. I can currently open youtube and google")
            speak("if you say tell me your name I will tell you my name")
            speak("if you say from wikipedia and then what to look for, I will summarize that wiki page for you")
            speak("if you say what time is it I will tell you the time")
            speak("if you say what day is it I will tell you the current day")
            speak("if you say open and then an application name, I will open the application. "
                  "I can currently open microsoft word and google chrome")
            speak("if you say thank you stop, I will take a rest until I am needed again")
            continue


if __name__ == '__main__':
    take_query()