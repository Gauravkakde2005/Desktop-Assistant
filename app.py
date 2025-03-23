from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import requests

app = Flask(__name__)

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Adjust speaking speed
engine.setProperty("volume", 1)  # Max volume

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        audio = recognizer.listen(source, phrase_time_limit=7)

    try:
        command = recognizer.recognize_google(audio, language="en-in")
        command = command.lower()
        return command
    except sr.UnknownValueError:
        return "Sorry, I could not understand."
    except sr.RequestError:
        return "Speech Recognition service is unavailable."

# Function to fetch weather details
def get_weather(city="Mumbai"):
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        description = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {description}."
    except:
        return "Couldn't fetch the weather details."

# Function to process commands
def process_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "search" in command:
        search_query = command.replace("search", "").strip()
        pywhatkit.search(search_query)
        return f"Searching {search_query} on Google"

    elif "play" in command:
        song = command.replace("play", "").strip()
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube"

    elif "wikipedia" in command:
        search_query = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(search_query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError:
            return "Multiple results found. Please be more specific."
        except wikipedia.exceptions.PageError:
            return "Couldn't find the topic on Wikipedia."

    elif "weather" in command:
        return get_weather()

    elif "notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    elif "exit" in command or "quit" in command:
        return "Goodbye!"

    else:
        return "Sorry, I didn't understand that command."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak_command():
    command = listen()
    response = process_command(command)
    speak(response)
    return jsonify({"command": command, "response": response})

if __name__ == "__main__":
    app.run(debug=True)
