import numpy as np

A = np.empty((2,3))
#print("A")
#print(A)

B = np.empty_like(A)
#print("B")
#print(B)

C= np.zeros((3,2))
#print("C")
#print(C)

D = np.ones((1,2))
#print("D")
#print(D.shape)

# SUma de matrices
# Declaro 2 matrices

A1 = np.matrix([[2,1,4],[5,7,2],[9,6,3]])
print(A1)
A2 = np.matrix([[2,1,4],[5,7,2],[9,6,3]])
matrixSuma = A1 + A2
print(matrixSuma)


matrixProd = A1.dot(A2)

print(matrixProd)