# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

print("Insira a temperatura em Fahrenheit")
f = input()
c = 5 * ((float(f)-32)/9)
print("Cº",c)