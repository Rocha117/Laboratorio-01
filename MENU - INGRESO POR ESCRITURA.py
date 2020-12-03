#import pyttsx3
#engine=pyttsx3.init()

#def tts(respuesta):
    #engine.setProperty("rate", 130)
    #engine.say(respuesta)
    #engine.runAndWait()

#////////////////////////////////////////

import wikipedia
wikipedia.set_lang("es")

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

#///////////////////////////////////////////////////////////////

nombre = str(input ("Nombre: ").lower())
apellido = str(input ("Apellido: ").lower())
print()
tema_buscar = input ("Buscar en Wikipedia: ").upper()
print ("Resultado de busqueda ...")
print()
buscador (tema_buscar)
otro_tema = input ("Buscar otro tema SI/NO: ").upper()
i=0
while i<1:
    if otro_tema=="SI":
        print()
        tema_buscar = input ("Buscar en Wikipedia: ")
        print ("Resultado de busqueda ...")
        print()
        buscador (tema_buscar)
        otro_tema = input ("Buscar otro tema SI/NO: ").upper()
    else:
        print("Gracias por visitar Wikipedia,", nombre.capitalize(), apellido.capitalize(),".")
        break
