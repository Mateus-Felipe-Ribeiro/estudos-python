# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

import math

x = int(input("1º numero inteiro: "))
y = int(input("2º numero inteiro: "))
z = float(input("numero real:"))

produto = (2*x)*(y/2)
soma = (3*x)+z
elevado = math.pow(z,3)
print("A:",produto)
print("B:",soma)
print("C:",elevado)
