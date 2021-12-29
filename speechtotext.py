import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import re
import requests
import json
import datetime

now = str(datetime.datetime.now())
print(now)

now = now.split()
print(now)

t = now[1].split(':')
hour = int(t[0])
min = int(t[1])
if hour < 12:
    r = sr.Recognizer()
    engine = p.init()
    engine.say("Good Morning!")

elif hour > 12 and hour <+16:
    r = sr.Recognizer()
    engine = p.init()
    engine.say("Good Morning!")


elif hour > 16 and hour<21:
    r = sr.Recognizer()
    engine = p.init()
    engine.say("Good Evening!")


r = sr.Recognizer()
engine = p.init()
engine.say("Hello! How are you doing?")
engine.runAndWait()
print("...Listening...")
engine.say('Listening')
with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)

    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")
    engine.say("What do you want me to do?")
    engine.runAndWait()


    try:
        r1 = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening..')
            engine.say('Listening')
            engine.runAndWait()
            audio = r1.listen(source)
            audio = r1.recognize_google(audio)
            if 'weather' in audio:

                res = requests.get(
                    'http://api.weatherapi.com/v1/current.json?key=7ac65f374a9f4c21957212815212712&q=India&aqi=yes')
                response = json.loads(res.text)
                # print(response)
                print("The temperature in Delhi: ", end=" ")
                print(response["current"]["temp_c"])
                r = sr.Recognizer()
                engine = p.init()
                engine.say("The temperature in Delhi: ")
                engine.say(response["current"]["temp_c"])
                engine.runAndWait()

            elif 'open' in audio:
                print('..')
                words = audio.split('open')
                print(words[-1])
                link = str(words[-1])
                link = re.sub(' ', '', link)
                engine.say('Opening')
                engine.say(link)
                engine.runAndWait()
                link = f'https://{link}.com'
                print(link)
                webbrowser.open(link)

            elif 'play songs on YouTube' in audio:
                url = 'https://www.youtube.com/results?search_query=play+songs'
                webbrowser.open(url)

            elif 'where is' in audio:
                print('..')
                words = audio.split('where is')
                print(words[-1])
                link = str(words[-1])
                link = re.sub(' ', '', link)
                engine.say('Locating')
                engine.say(link)
                engine.runAndWait()
                link = f'https://www.google.co.in/maps/place/{link}'
                print(link)
                webbrowser.open(link)

            elif 'list the tasks ' in audio:
                print('..')

                #link = f'https://roger.vercel.app/'
                print("Fetching data from TOODLE-DO Webapp...\n")
                engine.runAndWait()
                # webbrowser.open(link)

            elif 'Run my application' in audio:
                print('..')

                link = f'https://roger.vercel.app/'
                engine.say("Launching Roger")
                engine.runAndWait()
                print(link)
                # webbrowser.open(link)




            else:
                print(audio)
                print('Sorry, I do not understand that!')
                engine.say('Sorry, I do not understand that!')
                engine.runAndWait()
                #     recognised_text1 = r.recognize_google(text1)
    #     print(recognised_text1)
    #     if recognised_text1 == "play music":
    #         music()
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")