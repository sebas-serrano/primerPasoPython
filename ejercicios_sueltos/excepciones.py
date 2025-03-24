# exccepciones

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplicacion(num1, num2):
    return num2*num1

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("no se pude dividir por 0")

op1=(int(input("introduce el numero: ")))

op2=(int(input("introduce el numero: ")))

operacion=(input("introduzca la operacion que quiera hacer: "))

if operacion == "resta":
    print(resta(op1,op2))

elif operacion == "mult":
    print(multiplicacion(op1,op2))

elif operacion == "divide":
    print(divide(op1,op2))

elif operacion == "suma":
    print(suma(op1,op2))

else:
    print("operacion no encontrada")

print("termino ")    