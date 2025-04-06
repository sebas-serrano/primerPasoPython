"""
Find the last ten digits of the series, 990 exp 990 + 991 exp 991 + ...... + 1000 exp 1000
"""

def sefl_power(inicio, valor):
    if (valor == 1001):
        return 0
    else:
        sum = inicio + valor ** valor
    return sum


print(sefl_power(0, 990))