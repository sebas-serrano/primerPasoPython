""" 

Ejercicios de NUNPY

"""

import numpy as np

n = int(input("Ingrese la cantidad de filas de la matriz: "))
m = int(input("Ingrese la cantidad de columnas de la matriz: "))

A = np.empty((n,m))

for i in range(n):
    for j in range(m):
        A[i,j] = float(input("Ingrese el elemento ({},{}): ".format(i,j)))

print("\n=== Matriz ===")
print(A)