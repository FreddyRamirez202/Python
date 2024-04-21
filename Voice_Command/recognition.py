import speech_recognition as sr
import subprocess
import pyautogui

recognizer = sr.Recognizer()
proceso = None
saludo = """Hola, muchach@s, como están?"""

def ejecutar_comando(comando):
    global proceso
    if "open notepad" in comando:
        proceso = subprocess.Popen(['notepad.exe'])
    elif "say hello" in comando:
        pyautogui.write(saludo)
    elif "close notepad" in comando:
        proceso.terminate()

def escuchar_comandos():
    with sr.Microphone() as source:
        print("How can I help you?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        comando = recognizer.recognize_google_cloud(audio, language="en-EN")
        print(f"recognized command")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print(f"the command could not be understood")
    except sr.RequestError as e:
        print(f"error on request")
        
while True:
    escuchar_comandos()