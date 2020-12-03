import textoavoz
import wiki
from wiki import buscador

nombre = str(input("Nombre: ").lower())
apellido = str(input("Apellido: ").lower())
print()
tema_buscar = input("Buscar en Wikipedia: ").upper()
print("Resultado de busqueda ...\n")

textoavoz.tts(buscador(tema_buscar))
otro_tema = input("Buscar otro tema SI/NO: ").upper()
i = 0
while i < 1:
    if otro_tema == "SI":

        tema_buscar = input("\nBuscar en Wikipedia: ")
        print("Resultado de busqueda ...\n\n")

        textoavoz.tts(
            wiki.buscador(tema_buscar))
        otro_tema = input("Buscar otro tema SI/NO: ").upper()
    else:
        print("Gracias por visitar Wikipedia,",
              nombre.capitalize(), apellido.capitalize(), ".")
        break
