import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os
from datetime import datetime
import time
import pyjokes
import wikipedia
import pyautogui
import requests
import re
import time
import threading
from playsound import playsound
import psutil
import pygame
import shutil


def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

#! for text
# def text_command():
    # msg=input("Enter the command :")
    # print(f"you said {msg}")
    # return msg.lower()

#! for voice
def listen_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        audio=r.listen(source)
    
    try:
        msg=r.recognize_google(audio)
        print(f"you said {msg}")
        return msg.lower()
    
    except sr.WaitTimeoutError:
        print("No speech detected, say again")
        return ""
    
    except Exception as e:
        speak("I didn't get you, please say again")
        print(e)
        return ""


def wikipedia_search(query):
    try:
        results=wikipedia.search(query)
        if not results:
            speak("Sorry, I could not find any information")
            return
        topic=wikipedia.summary(results[0],sentences=2)
        return topic
    except wikipedia.DisambiguationError as e:
        print("Multiple options found, Please be more specific")
        print(e.options)
        return
    
def motivation_quotes():
    try:
        data=requests.get("replace your api here").json()
        quote=data[0]['q']
        author=data[0]['a']
        return f"{quote} - {author}"
    
    except:
        return "The only way to achieve the impossible is to believe it is possible."

def say_riddle():
    try:
        data=requests.get("replace your api here").json()
        riddle=data.get('riddle')
        answer=data.get('answer')
        return riddle,answer
    
    except:
        return "I speak without a mouth and hear without ears. What am I?", "An echo"

def find_weather(city):
    try:
        Api_key='replace your api key here'
        data=requests.get(f"").json()
        weather=data['weather'][0]['description']
        temperature=round(data['main']['temp']-273.15,2)
        return f"The temperature in {city} is {temperature}°C and the weather is {weather}"
    
    except:
        speak("internet connection problem")

def solve_math(msg):
    numbers=re.findall(r'\d+',msg)
    if "percent" in msg or "%" in msg:
        if len(numbers)<2:
            speak("Please provide both the percentage and the number")
            return
        
        percent=float(numbers[0])
        total=float(numbers[1])
        result=(percent/100)*total
        print(f"{percent} of {total} is {result}")
        speak(f"{percent} of {total} is {result}")
        return
    
    if len(numbers)<2:
        print("Please say valid math question")
        return
    
    a=int(numbers[0])
    b=int(numbers[1])

    if any(op in msg for op in ["add","addition","plus","+","sum"]):
        result=a+b
        operation="Addition"

    elif any(op in msg for op in ["subtract","minus","-"]):
        result=a-b
        operation="Subtraction"

    elif any(op in msg for op in ["divide","division","/","divided"]):
        if b==0:
            speak("divided by zero is not allowed")
            return
        result=a//b
        operation="Division"

    elif any(op in msg for op in ["multiply","multiplication","into","*"]):
        result=a*b
        operation="Multiplication"

    else:
        speak("Operation not recognized")
        return
    
    print(f"{operation} of {a} and {b} is {result}")
    speak(f"{operation} of {a} and {b} is {result}")

def extract_time(command):
    match=re.search(r'(\d{1,2}):(\d{2})',command)
    if match:
        hour=int(match.group(1))
        minute=int(match.group(2))
        if 0<= hour <24 and 0<= minute < 60:
            return hour,minute
        
    match = re.search(r'(\d{1,2})\s+(\d{1,2})', command)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2))
        if 0 <= hour < 24 and 0 <= minute < 60:
            return hour, minute
    
    return None, None


def alarm_thread(alarm_hour,alarm_minute):
    print(f"Alarm set for {alarm_hour}:{alarm_minute}")
    speak(f"Alarm set for {alarm_hour}:{alarm_minute}")
    while True:
        now=datetime.now()
        if now.hour==alarm_hour and now.minute==alarm_minute:
            speak("Alarm ringing...")
            playsound("replace alarm sound here")
            break
        time.sleep(20)

def set_alarm(command):
    alarm_hour,alarm_minute=extract_time(command)
    if alarm_hour is None:
        speak("Invalid time format. Please say in hours and minute format")
        time_str=listen_command()
        alarm_hour,alarm_minute=extract_time(time_str)
        if alarm_hour is None:
            speak("Invalid time format")
            return
    
    threading.Thread(target=alarm_thread,args=(alarm_hour,alarm_minute),daemon=True).start()


contacts={
    '''list of contacts here'''
}


pygame.mixer.init()
music_dir="your music path"
songs=[file for file in os.listdir(music_dir) if file.endswith('.mp3')]
current_index=0

def create_folder(folder_name):
    folder_path=os.path.join(os.path.expanduser("~"),folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        speak(f"{folder_name} Folder created successfully")
    else:
        speak(f"{folder_name} folder already exists")

def delete_folder(folder_name):
    folder_path=os.path.join(os.path.expanduser("~"),folder_name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        speak(f"{folder_name} folder deleted successfully")
    else:
        speak(f"{folder_name} folder does not exist")
    
def create_file(file_name):
    file_path=os.path.join(os.path.expanduser("~"),file_name)
    if not os.path.exists(file_path):
        with open(file_path,"w") as f:
            f.write("")
            speak(f"{file_name} file created successfully")
    else:
        speak(f"{file_name} file already exists")
    
def open_downloads():
    down_path=os.path.join(os.path.expanduser("~"),"Downloads")
    if os.path.exists(down_path):
        os.startfile(down_path)
        speak("Opening downloads folder")
    else:
        speak("Downloads folder not found")



def perform_task():
    speak("Hi I'm jarvis, your personal assistant say something")
    
    while True:
        command=listen_command()

        if "what is your name" in command:
            speak("Hi, I'm jarvis.")

        elif "introduce yourself" in command:
            speak("Hello, I am JARVIS, your personal assistant. I can help you with music, opening apps, managing files, and more!")
        
        elif "hi jarvis" in command or "hello" in command:
            speak("Hello! how can i help you")

        elif "what can you do" in command:
            speak("I can play music, open applications, manage files and folders, search the web, tell jokes, and motivate you!")

        elif "who made you" in command:
            speak("I was created by my amazing developer to assist with daily tasks and make life easier!")

        elif "how are you" in command:
            speak("I am doing great, thank you for asking!")

        elif "open youtube" in command:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Opening google")
            webbrowser.open("https://www.google.com")
        
        elif "chat gpt" in command:
            speak("Opening chat gpt")
            webbrowser.open("https://www.chatgpt.com")

        elif "open notepad" in command:
            speak("Opening notepad")
            os.system("notepad")
        
        elif "close notepad" in command:
            speak("Closing notepad")
            os.system("taskkill /F /IM notepad.exe")
        
        elif "open calculator" in command:
            speak("Opening calculator")
            os.system("calc")
        
        elif "close calculator" in command:
            speak("closing calculator")
            os.system("taskkill /F /IM ApplicationFrameHost.exe")

        elif "open paint" in command:
            speak("Opening paint")
            os.system("mspaint")
            
        elif "date" in command:
            now=datetime.now()
            date=now.strftime("%d-%m-%Y")
            print(f"Today date is {date}")
            speak(f"Today date is {date}")
        
        elif "day" in command or "which day is today" in command:
            day=datetime.now().strftime("%A")
            print(f"Today day is {day}")
            speak(f"Today day is {day}")

        elif "time" in command:
            now=datetime.now()
            curr_time=now.strftime("%I:%M:%p")
            print(f"current time is {curr_time}")
            speak(f"current time is {curr_time}")

        elif "joke" in command or "fun fact" in command:
            joke=pyjokes.get_joke(language="en")
            print(joke)
            speak(joke)
        
        elif "search" in command:
            search=command.replace("search for","").strip()
            if search=="":
                speak("Tell me topic to search")
            else:
                speak(search)
                webbrowser.open(f"https://www.google.com/search?q={search}")

        elif any(op in command for op in ['wikipedia','tell me about']):
            speak("Searching on wikipedia")
            info=wikipedia_search(command)
            print(info)
            speak(info)
        
        elif "screenshot" in command:
            speak("Taking screenshot")
            pyautogui.screenshot('screenshot.png')
            speak("Screenshot saved")

        elif "quote" in command or "motivate me" in command:
            quote=motivation_quotes()
            print(quote)
            speak(quote)

        elif "riddle" in command:
            riddle,answer=say_riddle()
            print(riddle)
            speak(riddle)
            time.sleep(3)
            print(answer)
            speak(answer)

        elif any(op in command for op in ["mail","email","gmail"]):
            speak("Opening email")
            webbrowser.open("https://mail.google.com") 

        elif "weather" in command:
            # city=command.replace("tell me the weather of","").strip()
            speak("which city do you want the weather for?")
            city=listen_command()
            info=find_weather(city)
            print(info)
            speak(info)

        elif any(op in command for op in["plus","add", "minus","subtract", "multiply", "into", "divided","percent", "+", "-", "*", "/", "%"]):
            solve_math(command)

        elif "set alarm" in command:
            set_alarm(command)

        elif "send whatsapp message to" in command:
            name=command.replace("send whatsapp message to","").strip().lower()
            if name in contacts:
                speak(f"what you want to send to {name}")
                msg=listen_command()
                try:
                    pywhatkit.sendwhatmsg_instantly(contacts[name],msg)
                    speak(f"message send to {name} successfully")
                except Exception as e:
                    print(e)
                    speak("Sorry, i could not send the message")
            else:
                speak(f"contact {name} is not found in my contacts")

        elif "check battery" in command:
            battery=psutil.sensors_battery()
            percent=battery.percent
            plugged=battery.power_plugged
            if plugged:
                print(f"The battery is at {percent} percent and plugged in")
                speak(f"The battery is at {percent} percent and plugged in")
            else:
                print(f"the battery is at {percent} percent")
                speak(f"the battery is at {percent} percent")

        elif "play music" in command:
            current_index=0
            pygame.mixer.music.load(os.path.join(music_dir,songs[current_index]))
            pygame.mixer.music.play()
            speak("Playing music")
        
        elif "next song" in command:
            current_index+=1
            if current_index>=len(songs):
                current_index=0
            speak("playing next song..")
            pygame.mixer.music.load(os.path.join(music_dir,songs[current_index]))
            pygame.mixer.music.play()

        elif "pause music" in command:
            pygame.mixer.music.pause()
            speak("Music paused")
        
        elif "resume music" in command:
            pygame.mixer.music.unpause()
            speak("Music resumed")
        
        elif "stop music" in command:
            pygame.mixer.music.stop()
            speak("Music stopped")
        
        elif "increase volume" in command:
            pyautogui.press("volumeup")
        
        elif "decrease volume" in command:
            pyautogui.press("volumedown")

        elif "mute volume" in command:
            pyautogui.press("volumemute")

        elif "create a folder" in command:
            folder_name=command.replace("create a folder","").strip() or "Newfolder"
            create_folder(folder_name)
        
        elif "delete folder" in command:
            folder_name=command.replace("delete folder","").strip() or "Newfolder"
            delete_folder(folder_name)

        elif "play" in command or "on youtube" in command:
            song=command.replace("play","").replace("on youtube","").strip()
            if song:
                speak(f"Playing {song}")
                pywhatkit.playonyt(song)
            else:
                speak("Please tell me again")

        elif "create a file" in command:
            file_name=command.replace("create a file","").strip() or "Newfolder"
            create_file(file_name)

        elif "open downloads" in command:
            open_downloads()
        
        elif "sleep" in command:
            speak("Going to sleep. say wake up to activate me")
            while True:
                wake_command=listen_command()
                if "wake up" in wake_command:
                    speak("I am awake now")
                    break
        
        elif "thank you" in command:
            speak("You're welcome . Let me know if you need something")

        elif "bye" in command or "stop" in command:
            speak("Good bye! have a nice day")
            break

perform_task()