import speech_recognition
import wiki
import textoavoz
import sys

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("\nDiga su nombre: ")
    nombre = recognizer.listen(source)

nombre = recognizer.recognize_google(nombre, language="es").title()
print("\nNombres: " + nombre)

control = "sí"

while control == "sí" or control == "si":

    try:
        with speech_recognition.Microphone() as source:
            print(f"\n{nombre} ¿Qué desea buscar?: \n")
            busqueda = recognizer.listen(source)

        tema_buscar = recognizer.recognize_google(
            busqueda, language="es").upper()

        print("Tema: " + tema_buscar)
        print("\n")
        print("Buscando...")
        print("--------------------------------------------------------------------------------------------------------")

        w = wiki.buscador(tema_buscar)
        textoavoz.tts(w)

    except:
        print("No se ha encontrado la busqueda")

    with speech_recognition.Microphone() as source:
        sys.stdout.flush()
        print("--------------------------------------------------------------------------------------------------------")
        print(f"Hey {nombre} desea realizar otra busqueda? si/no ")
        contr = recognizer.listen(source)

    #controlar = recognizer.recognize_google(contr, language = 'es', show_all=True).lower()
    controlar = recognizer.recognize_google(
        contr, language="es").lower()

    control = controlar


print(f"Gracias por usar este buscador, {nombre}")
