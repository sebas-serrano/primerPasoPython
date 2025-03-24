
def ejercicio1 ():
    numero  = float(input("Ingrese un numero real "))

    if(numero > 0):
        print("El numero es mayor a 0")
    elif (numero < 0):
        print("El numero es menor a 0")
    else:
        print("El numero es igual a 0")

ejercicio1()

def ejercicio2():
    nombre  = input("Ingrese su nombre ")
    if(len(nombre) > 10):
        print("Su nombre tiene mas de 10 caracteres")
    else:
        print("Su nombre no tiene mas de 10 caracteres")

ejercicio2()

def ejercicio3():
    
    nombre  = input("Ingrese su nombre ")
    print("Su nombre tiene mas de 10 caracteres") if(len(nombre) > 10)  else print("Su nombre no tiene mas de 10 caracteres")

ejercicio3()
print("Mallorca" >= "Maldivas")