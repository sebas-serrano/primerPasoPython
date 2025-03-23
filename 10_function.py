### Functions ###

def my_function ():
    print("esto es una funcion")
def my_second_function (val1, val2):
    return val1 + val2

my_function()
# print(my_second_function(2,56))

def a ():
    print("")

def bucles():
    a = 0
    for letra in "bbbabbb":
        a+=1
        if letra != "a":
            pass
        else: 
            print(letra)
    
#bucles()

# Funcion que devuelte una lista de numeros pares 
def nunerosPares(cantidad):
    mi_lista = []  # Lista vacía
    for n in range(1,cantidad):
        if n % 2 == 0:
            mi_lista.append(n)
    yield mi_lista 
    #return mi_lista


#print(nunerosPares(30))


def devuelve_ciudaddes(*ciudades):
    for elementos in ciudades:
        for letra in elementos:
            yield letra

def devuelve_ciudaddes_optimizado(*ciudades):
    for elementos in ciudades:
            yield from elementos


ciudades = devuelve_ciudaddes_optimizado ("Miami", "Pde", "Santa Fe")
print(next(ciudades))
print(next(ciudades))






