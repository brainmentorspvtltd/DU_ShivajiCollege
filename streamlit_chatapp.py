import streamlit as st
from datetime import datetime as dt
import random
import os, glob

greetIntent = ["hello","hi","hey","hello there","hi there"]
dateIntent = ["date","date please","tell me date","what's today's date"]
timeIntent = ["time","time please","tell me time","what's the time"]
songIntent = ["play song","song","play music"]

st.title("This is chat app...")
st.write("Simple If Else Based Python Chat App")

form = st.form("chat_form")
msg = form.text_input("Enter your message : ")
btn = form.form_submit_button("Submit")

msg = msg.lower()

if btn:
    if msg in greetIntent:
        st.write("Hello User...")
    elif msg in dateIntent:
        date = dt.now().date()
        st.write("Date is : {}".format(date.strftime("%d %b, %Y, %a")))
    elif msg in timeIntent:
        time = dt.now().time()
        st.write("Time is : {}".format(time.strftime("%I:%M:%S,%p")))
    elif msg in songIntent:
        path = r"D:\Batches\Songs\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        os.startfile(random.choice(songs))    
    elif msg == "bye":
        st.write("Bye User")
    else:
        st.write("I don't understand")









