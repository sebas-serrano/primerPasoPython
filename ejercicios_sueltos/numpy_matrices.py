""" 

Ejercicios de Matrices con NUNPY

"""

import numpy as np

def cargarMatrizXTeclado():    
    """
    Esta funcion crea una matris. Las dimensiones las carga el usuario por teclado. Y el usuario
    agrega los elemntos de dicha matriz por teclado.

    Args:
        Sin entradas

    Returns:
        Retorna la matriz creada.         
    
    """
    n = int(input("Ingrese la cantidad de filas de la matriz: "))
    m = int(input("Ingrese la cantidad de columnas de la matriz: "))

    A = np.empty((n,m))

    for i in range(n):
        for j in range(m):
            A[i,j] = float(input("Ingrese el elemento ({},{}): ".format(i,j)))
    
    return A



print("\n=== Matriz ===")
A = cargarMatrizXTeclado()
print("\n=== Imprimimos el resultado ===")
print(A)

