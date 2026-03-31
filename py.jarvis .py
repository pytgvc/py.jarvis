
import tkinter as tk
import threading
import speech_recognition as sr
import webbrowser
import pyttsx3
import studylibrary

recognizer = sr.Recognizer()
# --- GUI setup ---
root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("600x400")

output_label = tk.Label(root, text="Initializing Jarvis...", font=("Arial", 14), wraplength=500, justify="center")
output_label.pack(pady=40)



def speak(text):
    engine = pyttsx3.init()
    engine .say(text)
    engine .runAndWait()
    engine .stop()

def processCommand(c):  
    c = c.lower()
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    

    elif "what is python" in c.lower() or "python" == c.lower().strip():
        speak("Python is a high level interpreted programming language known for its simple and readable syntax.")

    elif "who created python" in c.lower() or "who made python" in c.lower():
        speak("Python was created by Guido van Rossum in the late 1980s.")

    elif "what is a variable" in c.lower() or "variable" in c.lower():
        speak("In Python, variables are symbolic names that refer to objects or values stored in memory. They allow you to assign descriptive names to data.")

    elif "what is a function" in c.lower() or "function" in c.lower():
        speak("A function in Python is a named reusable block of code that performs a specific related action or task. The code block within the function must be indented.")

    elif "what are libraries" in c.lower() or "library" in c.lower() or "libraries" in c.lower():
        speak("Python libraries are collections of pre-written modules that make coding faster, cleaner and more efficient by providing ready-to-use solutions.")

    elif "importance of python" in c.lower() or "importance" in c.lower() or "tell me importance" in c.lower():
        speak("Python libraries make coding faster, cleaner and more efficient for different domains such as data science, web development, machine learning and automation.")

   

    # --- Study playlists ---
    elif "study" in c or "course" in c or "playlist" in c or "play" in c:
        topic = c.replace("study", "").replace("course", "").replace("playlist", "").replace("play","").strip()
        if topic in studylibrary.study:
            webbrowser.open(studylibrary.study[topic])
            speak(f"Opening {topic} playlist")
        else:
            speak("Sorry, I don't have that study playlist")



def listen_loop():
    speak("Jarvis initialized and ready.")
    while True:
        try:

            with sr.Microphone() as source:
                print("Listening for ...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            print("you said:", word)
            if "jarvis" in word.lower():
                speak("Yes")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command)
        except Exception as e:
            print("Error:", e)


# Run listening loop in a background thread so GUI stays responsive
threading.Thread(target=listen_loop, daemon=True).start()

root.mainloop()
