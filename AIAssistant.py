import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
print("Initializing JARVIS")

MASTER="Deepraj"
engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#it will pronunce the string.
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#it will wish according to time:-   
def wishMe():
    hour= int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("GOOD Morning" + MASTER)
        
    elif hour>=12 and hour<18:
        speak("GOOD Afternoon"+ MASTER)
        
    else:
        speak("GOOD Evening"+ MASTER)

# this will take command from the microphone

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0)
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Please Say That Again")
        query=None
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("user's email", 'PASSWORD')
    server.sendmail('user email', to, content)
    server.close()

#To shut down the computer
# def shutdown(): 

# if shutdown == 'no': 
#     exit() 
# else: 
#     os.system("shutdown /s /t 1") 

#main commands
speak("Initializing JARVIS..")
wishMe()
speak("I am JARVIS, How can I help you?")
query=takeCommand()



#Logic for  executing tasks
if 'wikipedia' in query.lower():
    speak('Serching wikipedia.')
    print("Serching wikipedia...")
    query= query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)
    
    
elif 'open youtube' in query.lower():
    url = "youtube.com"
    print("Opening YouTube..")
    speak('Opening YouTube For You')
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = "google.com"
    print("Opening Google..")
    speak('Opening Google For You')
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


elif 'play music' in query.lower():
    url= "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbUhuZUdJdnVBQ25XcmhMUHpkMTRRVA%3D%3D"
    print('Opening YouTube Music......')
    speak("Opening YouTube Music for you")
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'what is the time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M,%S")
    speak(f"Hello {MASTER} The Time is {strTime}")
elif 'open wikipedia' in query.lower():
    url= "https://www.wikipedia.org/"
    print('Opening Wikipedia')
    speak("Opening Wikipedia for you")
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open github' in query.lower():
    url= "https://github.com/"
    print('Opening Github..')
    speak("Opening Github for you")
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open Amazon' in query.lower():
    url= "https://www.amazon.in/?ref=icp_country_us_t1"
    print('Opening Amazon..')
    speak("Opening Amazon for you")
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open Udemy' in query.lower():
    url= "https://www.udemy.com/"
    print('Opening Udemy..')
    speak("Opening Udemy for you")
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
# for email sending function first change setting of your email and set it to control access to less secure app
elif 'email to' in query:
            try:
                speak("Sir, give me your message")
                print('Give message.......')
                content = takeCommand()
                to = "reciever email"
                sendEmail(to, content)
                print('Sending mail........')
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry master . I am not able to send this email")
    
