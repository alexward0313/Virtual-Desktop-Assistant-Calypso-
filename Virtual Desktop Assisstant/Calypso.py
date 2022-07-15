import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from datetime import date

listener = sr.Recognizer()
#setting the engine's voice response
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("rate", 196)
engine.setProperty("volume", 2.7)
engine.setProperty("voice", voices[1].id)
engine.say("Hello Master")
engine.say("How may I serve you today?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
#has the speech recognizer listen to the source
    try:
        with sr.Microphone() as source: 
            print("Yes Master...?")
            voice = listener.listen(source)
            #this is where the input goes
            command = listener.recognize_google(voice)
            #will only respond to calypso
            command = command.lower()
            if "calypso" in command:
                command = command.replace("calypso", "")
                print(command)
    except:
        pass

    return command

#command for playing music
def run_calypso():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", " ")
        print(song)
        talk("Playing: " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M %p")
        print(time)
        talk("The current time is: " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "date" in command:
        today = date.today().strftime("%b, %d")
        print(today)
        talk("Today is: " + today)
    
        

run_calypso()
