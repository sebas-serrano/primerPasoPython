"""
Work out the first ten digits of the sum of the following one-hundred 
-digit numbers.
"""

def abri_archivo():
    # Abrir un archivo con open() y close()
    file_handler = open('euler/numero.txt')
    return file_handler

def large_sum(file):
    suma = 0
    for i in file:
        suma += int(i.strip()) 
    return str(suma)[:10]

file = abri_archivo()
print(large_sum(file))