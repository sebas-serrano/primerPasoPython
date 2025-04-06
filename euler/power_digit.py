"""
What is the sum of the digits of the number 2 to the power of 1000
"""

def two_to_power():
    exponent = 2 ** 1000
    sum = 0
    cantidad_digitos = len(str(exponent))    
    for i in (str(exponent)):
        sum += int(i)
    return sum

print(two_to_power())