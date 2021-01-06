import pyttsx3 #you have to install this module
import datetime # no need to install to ,it is build in module 
import speech_recognition as sr #we use (takeCommand name) function in this project,we have to install this module
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')# we use sapi5 for getting voices ,windows provide some API's for  voices, inbuild voice present in windows and you can use it
voices = engine.getProperty('voices')# in this point get property getting the voice
# print(voices[0].id) # we check which voice available in this system with the help of id.
voices = engine.setProperty('voice',voices[0].id)# in this point of set property set the voice ,


def speak(audio):
    engine.say(audio)# engine say this audio which come from this speak function string
    engine.runAndWait()# This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.


def wishme():# this function call from main method
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am jayshree sir, Please tell me how can i help you")


def takeCommand():
    '''
       it take microphone input from the user and return string output 
    '''
    r = sr.Recognizer()#this recognizer class will help us to recognize our audio
    with sr.Microphone() as source: # this line represent that she's listening to our voice 
        print("Listening.....") # if she listening it printed listening...
        r.pause_threshold = 1 # it means if we talk and taking gap in talking ,this function do not exit ,that's why we taking 1 second pause threasold.
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        
        return query


if __name__ == "__main__":
    # speak("Jayshree is now become a softwaer Developer")
    wishme() # in this point we call wishme function
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)# taking user input
            speak("According to wikipedia")
            print(results) # and written data about user input
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)# list of all songs play
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))# play first song or your can make list of random song
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") # written time in string formate
            speak(f"the time is {strTime}") #speak time

        elif 'open code' in query:
            codePath = "C:\\Users\\JAYSHREE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        



