# -*- coding: utf-8 -*-
import textoavoz
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

    resp2 = "".join(reslist)
    print(resp2)
    return(resp2)
