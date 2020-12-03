import pyttsx3

engine = pyttsx3.init()


def tts(respuesta):
    engine.setProperty("rate", 130)
    engine.say(respuesta)
    engine.runAndWait()
