# Desktop Assistant

## Introduction
The **Desktop Assistant** is a voice-controlled AI assistant built using **Python** and **Flask**. It allows users to perform various tasks using voice commands, including searching on Google, playing YouTube videos, fetching weather updates, opening applications, and more. The assistant uses **Speech Recognition** to process voice commands and responds using **Text-to-Speech (TTS)**.

## Features
- **Speech Recognition**: Converts voice input into text using `speech_recognition`.
- **Text-to-Speech (TTS)**: Uses `pyttsx3` to provide voice responses.
- **Google Search & YouTube Playback**: Searches the web and plays YouTube videos.
- **Wikipedia Summaries**: Fetches brief summaries of topics from Wikipedia.
- **Weather Updates**: Provides real-time weather updates using the OpenWeather API.
- **Time & Date Retrieval**: Tells the current time and date.
- **Application Launcher**: Opens Notepad and Calculator.
- **Flask Web Interface**: A simple web UI to interact with the assistant.

## Technologies Used
- **Python** (Core language)
- **Flask** (Web framework)
- **SpeechRecognition** (For voice input processing)
- **pyttsx3** (Text-to-Speech engine)
- **pywhatkit** (For YouTube and Google searches)
- **Wikipedia API** (For fetching summaries)
- **OpenWeather API** (For weather updates)
- **Web Browser Module** (For opening websites)
- **OS Module** (For launching system applications)

## Installation & Setup
### Prerequisites
Make sure you have **Python 3.x** installed. Then, install the required dependencies:

```sh
pip install flask speechrecognition pyttsx3 pywhatkit wikipedia requests
```

### Running the Assistant
1. Clone the repository:
   ```sh
   git clone https://github.com/Gauravkakde2005/emotion-detector-.git
   ```
2. Navigate to the project folder:
   ```sh
   cd emotion-detector-
   ```
3. Run the Flask application:
   ```sh
   python app.py
   ```
4. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
5. Use the web interface to interact with the assistant!

## Usage
- **Say "search [query]"** → Searches Google for the given query.
- **Say "play [song name]"** → Plays the song on YouTube.
- **Say "wikipedia [topic]"** → Fetches Wikipedia summary.
- **Say "time" or "date"** → Gets the current time or date.
- **Say "weather"** → Fetches weather details for Mumbai.
- **Say "notepad" or "calculator"** → Opens Notepad or Calculator.
- **Say "exit" or "quit"** → Closes the assistant.

## API Endpoints
| Endpoint        | Method | Description                      |
|---------------|--------|--------------------------------|
| `/`           | GET    | Returns the web UI home page.  |
| `/speak`      | POST   | Processes voice commands.     |

## Future Enhancements
- Add **support for more applications** (e.g., email, calendar, messaging apps).
- Implement **multi-language support**.
- Enhance **machine learning-based command recognition**.

## Contributing
Feel free to contribute! Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

---
### Developed by [Gaurav Kakde](https://github.com/Gauravkakde2005) 🚀
