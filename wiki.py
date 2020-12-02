# -*- coding: utf-8 -*-
import wikipedia
wikipedia.set_lang("es")


def buscador(pregunta):
    respuesta = wikipedia.summary(pregunta, sentences=5)
    reslist = list(respuesta)
    k = "["
    while (k in reslist):
        i = reslist.index(k)

        reslist.remove(k)
        reslist.remove(reslist[i])
        reslist.remove(reslist[i])

    res2 = "".join(reslist)
    print(res2)


pregunta = str(input("Escribe lo que quieres buscar: "))

buscador(pregunta)
