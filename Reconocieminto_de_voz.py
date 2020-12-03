import speech_recognition
import wikipedia


wikipedia.set_lang("es")

recognizer = speech_recognition.Recognizer()

def buscador(tema_buscar):
    respuesta = wikipedia.summary(tema_buscar, sentences=5)
    reslist = list(respuesta)
    k = "["
    while (k in reslist):
        i = reslist.index(k)

        reslist.remove(k)
        reslist.remove(reslist[i])
        reslist.remove(reslist[i])

    res2 = "".join(reslist)
    print(res2)

with speech_recognition.Microphone() as source:
	    print("\nDiga su nombre: ")
	    nombre = recognizer.listen(source)

nombre =recognizer.recognize_google(nombre, language = "es").title()
print("\nNombres: " + nombre )

control = "sí"

while  control == "sí" or control == "si":

	try:
		with speech_recognition.Microphone() as source:
		    print(f"\n{nombre} ¿Qué desea buscar?: \n")
		    busqueda = recognizer.listen(source)

		tema_buscar = recognizer.recognize_google(busqueda, language = "es").upper()

		print("Tema: " + tema_buscar)
		print("\n")
		print("Buscando...")
		print("--------------------------------------------------------------------------------------------------------")

		buscador(tema_buscar)

	except:
		print("No se ha encontrado la busqueda")


	with speech_recognition.Microphone() as source:
		print("--------------------------------------------------------------------------------------------------------")
		print(f"Hey {nombre} desea realizar otra busqueda? si/no ")
		contr = recognizer.listen(source)

	#controlar = recognizer.recognize_google(contr, language = 'es', show_all=True).lower()
	controlar = recognizer.recognize_google(contr, language = "es").lower()
	print(controlar)

	control = controlar


print(f"Gracias por usar este buscador, {nombre}")
