# agents/voice_interface.py

import pyttsx3
import speech_recognition as sr

class VoiceInterface:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # You can customize this
        self.recognizer = sr.Recognizer()
        print("[VoiceInterface] Initialized voice engine.")

    def speak(self, text):
        """
        Convert text to speech.
        """
        print(f"[VoiceInterface] Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, timeout=5):
        """
        Capture voice input and convert to text.
        """
        with sr.Microphone() as source:
            print("[VoiceInterface] Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                command = self.recognizer.recognize_google(audio)
                print(f"[VoiceInterface] Heard: {command}")
                return command
            except sr.WaitTimeoutError:
                print("[VoiceInterface] Listening timed out.")
            except sr.UnknownValueError:
                print("[VoiceInterface] Could not understand the audio.")
            except sr.RequestError as e:
                print(f"[VoiceInterface] Request error: {e}")
            return None


# Sample usage
if __name__ == "__main__":
    vi = VoiceInterface()
    vi.speak("Hello, how can I assist you today?")
    command = vi.listen()
    
    if command:
        vi.speak(f"You said: {command}")
    else:
        vi.speak("Sorry, I didn't catch that.")
