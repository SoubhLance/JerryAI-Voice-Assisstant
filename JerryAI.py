
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import random
import bs4
import googletrans
from googletrans import Translator
import pyautogui
import pywhatkit
from bs4 import BeautifulSoup
import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
        speak("Good Morning!")
     elif hour>=12 and hour<18:
        speak("Good Afternoon!")
     else:
        speak("Good Evening!")
     speak("I am Jerry Sir. I am Here to assist You. Please, tell me how may I help You")
     #speak("I am Friday Sir. I am Here to assist You. Please, tell me how may I help You")

def takeCommand():
    # It is taking input from the user and printing it
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}")
    except Exception as Error:
        print("Say that again, please...") 
        return None
    return query


def Screenshot():
    speak("ok boss,What should i name the file?")
    path=takeCommand()
    path1name = path +".png"
    path1 = "D:\AI\SS" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("D:\\AI")
    speak("Here is your screen shot")



def temperature(query):
    query = takeCommand().lower()
    city = query.split("in", 1)
    try:
        url = f"https://www.qoog1e.com/search?q=weather+in+{city[1]}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            region = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
            temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
            if region and temp:
                speak(f"It's currently {temp.text} in {region.text}")
            else:
                speak("Sorry, I couldn't find the weather information for that location.")
        else:
            speak("Sorry, I couldn't fetch the weather information right now. Please try again later.")
    except Exception as e:
        print("An error occurred:", e)
        speak("Sorry, I encountered an error while fetching the weather information.")

def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='hi')
            print(f"User said: {query}")
        except Exception as Error:
            print("Say that again please...") 
            return None
    return query

def Tran():
    speak("Tell me the line!")
    line = TakeHindi()
    traslate = Translator()
    ans = traslate.translate(line)
    Text = ans.text
    print("       ")
    print(Text)
    speak(Text)

def Whatsapp():
    speak("Tell me the name of the Person!")
    wname = takeCommand().lower()

    if 'soumya' in wname:
        speak("Tell me the Message!")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+919883738822",msg)
        speak("Ok! Sir, Sending sending message")
    elif 'souro' in wname:
        speak("Tell me the Message!")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly("+919007603333",msg)
        speak("Ok! Sir, Sending sending message")
    else:
        speak("Ok Tell me the phone number")
        num = int(takeCommand())
        ph = '+91' + num
        speak("Tell me the Message!")
        msg = takeCommand()
        pywhatkit.sendwhatmsg_instantly(ph,msg)
        speak("Ok! Sir, Sending sending message")

def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='hi')
            print(f"User said: {query}")
            speak(f"user said: {query}")
        except Exception as Error:
            print("Say that again please...") 
            return None
    return query



#Tasks
def TaskEXE():
    if __name__== "__main__":
        wishMe()
        while True:
            query = takeCommand().lower()
            #Logic executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            elif 'hello jerry' in query:
                speak("Hello Sir, What can i do for You")
            
            elif 'hello' in query:
                speak("Hello Sir, What can i do for You")
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("www.google.com")
            
            elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")
            
            elif 'open gmail' in query:
                webbrowser.open("mail.google.com")
            
            elif 'open college' in query:
                webbrowser.open("www.srmist.edu.in")
            
            elif 'open github' in query:
                webbrowser.open("www.github.com/SoubhLance")
            
            elif 'open linkedin' in query:
                webbrowser.open("www.linkedin.com/in/soubhik-sadhu-0427b4288")

            elif 'play music' in query:
                    speak("Sir play music from, offline,  or look, online")
                    choice= takeCommand().lower()
                    if "offline" in choice:
                        music_dir = 'D:\\SONGS\\Music'
                        songs = os.listdir(music_dir)
                        #print(songs)
                        a=random.randint(1,1400)
                        os.startfile(os.path.join(music_dir, songs[a]))
                    else:
                        speak("Tell the name of the music")
                        musicname=takeCommand()
                        pywhatkit.playonyt(musicname)
                    speak("Your Song has been started, Enjoy Sir")  
            
            elif 'meditation' in query:
                    word="D:\Bhajans"
                    msword = os.listdir(word)
                    #os.startfile(word)
                    b=random.randint(1,222)
                    os.startfile(os.path.join(word, msword[b]))
                    speak("Opened Sir!") 
           
            elif 'the time' in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, The time is {strtime}")
            
            elif 'show my youtube channel' in query:
                webbrowser.open("www.youtube.com/channel/UCVu_kIJI9LqbQqBJKe-8YwQ")
            
            elif 'tell about yourself' in query:
                speak("Hello Sir, Allow me to introduce myself, I am Jerry Your Personal Artificial Intelligence AI assisstant")
                speak("I am here to make your life easier, I can perform several tasks for you 24 hours a day and 7days a week")
                speak("importing all preferences from home interface.....Thank You")
            
            elif 'search in youtube' in query:
                speak("Ok Sir, This is what i found in your search")
                query=query.replace("jerry","")
                query=query.replace("search in youtube","")
                web='https://www.youtube.com/results?search_query=' + query
                link=web
                print(link)
                webbrowser.open(link)
                speak("Done sir")
            
            elif 'search in google' in query:
                speak("Ok Sir, This is what i found in your search")
                query=query.replace("jerry","")
                query=query.replace("search in google","")
                pywhatkit.search(query)
                speak("Done Sir")
            
            elif 'exit' in query:
                speak("Bye Sir, Nice Meeting You")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    speak("Have a nice Day!")
                elif hour>=12 and hour<18:
                    speak("Have a nice Day!")
                else:
                    speak("Hope Your Day Went well!")
                break
            
            elif 'who built you' in query:
                speak("I was built by Team Code Crusaders")
            
            elif 'who created you' in query:
                speak("I was built by Team Code Crusaders")
            
            elif 'thank you' in query:
                speak("It's my Pleasure, Sir")
            
            elif 'run speed test' in query:
                webbrowser.open("www.speedtest.net")
                speak("Checking the Speed Sir, Just a second")
                speak("Done Sir")
            
            elif 'take screenshot' in query:
                Screenshot()
            elif 'temperature today' in query:
                temperature(query)
                
            elif 'google search' in query:
                import wikipedia as googleScrap
                query=query.replace("jerry","")
                query=query.replace("google search","")
                query=query.replace("google","")
                speak("This is what i found on the web!")

                try:
                    pywhatkit.search(query)
                    result=googleScrap.summary(query,3)
                    speak(result)
                except:
                    speak("No Callable Data Available!")

            elif 'thank you' in query:
                speak("It's my Pleasure, Sir")
            
            elif 'thank' in query:
                speak("It's my Pleasure, Sir")

            elif 'run speed test' in query:
                webbrowser.open("www.speedtest.net")
                speak("Checking the Speed Sir, Just a second")
                speak("Done Sir")
            
            elif 'send message' in query:
                Whatsapp()
            elif 'whatsapp' in query:
                Whatsapp()

            elif 'translator' in query:
                Tran()
            
            elif 'translater' in query:
                Tran()

            elif 'take a break' in query:
                speak("Ok Sir! You can call me again Whenever you need me!")
                speak("Just say wake up jerry!")
                break
           
            elif 'you need a break' in query:
                speak("Ok Sir! You can call me again Whenever you need me!")
                speak("Just say wake up jerry!")
                break

            elif 'exit' in query:
                speak("Bye Sir, Nice Meeting You")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    speak("Have a nice Day!")
                elif hour>=12 and hour<18:
                    speak("Have a nice Day!")
                else:
                    speak("Hope Your Day Went well!")
                break



TaskEXE()
