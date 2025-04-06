"""
Find the sum of all the numbers that can be written as the sum of fourth powers of their digits.
"""

def digit_fourth_power():
    suma = 0
    for numero in range(2, 100000):  #  dígitos
        original = numero
        digitos = []
        while numero > 0:
            digitos.insert(0, numero % 10)
            numero //= 10
        val1 = sum(d ** 5 for d in digitos)
        if val1 == original:
            suma += val1
    return suma

print(digit_fourth_power())
