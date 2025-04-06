def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sumar_primos(limite):
    suma = 0
    for i in range(2, limite):
        if es_primo(i):
            suma += i
    return suma

print(sumar_primos(2_000_000))
