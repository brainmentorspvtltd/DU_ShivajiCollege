#Simple ChatBot Using If Else
from datetime import datetime as dt
import random
import os, glob

greetIntent = ["hello","hi","hey","hello there","hi there"]
dateIntent = ["date","date please","tell me date","what's today's date"]
timeIntent = ["time","time please","tell me time","what's the time"]
songIntent = ["play song","song","play music"]

chat = True

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User...")

    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is :",date.strftime("%d %b, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is :",time.strftime("%H:%M:%S,%p"))
    elif msg in songIntent:
        path = r"D:\Batches\Songs\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        os.startfile(random.choice(songs))
    
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
