"""
Leer todas las líneas del archivo.

Contar cuántos comentarios positivos, negativos y neutrales hay.
Palabras positivas: ["excelente", "perfecto", "buen", "satisfecho", "recomiendo"]
Palabras negativas: ["mal", "tarde", "pésima"]

Para ello, vas a usar una lista de palabras clave positivas y negativas.

Imprimir el resultado por pantalla.
"""

def abri_archivo():
    # Abrir un archivo con open() y close()
    file_handler = open('c:/texto_prueba.txt')
    return file_handler

# Leer todas las líneas del archivo.
def imprimir_lineas(file):
    for linea in file:
        print(linea)

# Palabras positivas: ["excelente", "perfecto", "buen", "satisfecho", "recomiendo"]
def leer_positivo(file):
    positivo = 0
    for linea in file:
        palabras = []
        palabras = linea.split(' ')
        for p in palabras:
            if (p == "excelente" or p == "perfecto" or p == "buen" or p == "satisfecho" or p == "recomiendo"):         
                positivo = positivo +1
    return positivo

# Palabras negativas: ["mal", "tarde", "pésima"]
def leer_negativos(file):
    negativos = 0
    for linea in file:
        palabras = []
        palabras = linea.split(' ')
        for p in palabras:
            if (p == "mal" or p == "tarde" or p == "buen" or p == "pésima" or p == "recomiendo"):         
                negativos = negativos +1
    return negativos

file = abri_archivo()
#imprimir_lineas(file)
print("Palabras positivos: ",leer_positivo(file))
file = abri_archivo()
print("Palabras negativos: ",leer_negativos(file))