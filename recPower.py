def recPower(a,b):
    if b == 0:
        return 1
    else:
        return a * recPower(a,b-1)

r = recPower(3,2)
print(r)

# Esta função calcula a potência de base "a" e expoente "b" de maneira recursiva.
# Devido a multiplicação no pior caso (else), os valores armazenados são multiplicados entre eles mesmos,
# assim formando uma potência de expoente 3, e estes valores podem ser totalmente arbitrários.