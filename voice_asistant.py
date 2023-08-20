import re
import pyttsx3
import pyaudio
import speech_recognition as sr

def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            print("No me ha dicho su nombre....")
    return name
def main():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")

    engine.say("Hola, Como te llamas")
    engine.runAndWait()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
        name = identify_name(text)
        if name:
            engine.say("Encantado de conocerte, {}".format(name))
        else:
            engine.say("Pues mira, la verdad que no te entiendo ni mrda, puedes quitarte la chala de la boca?")
        engine.runAndWait()

if __name__ == "__main__":
    main()