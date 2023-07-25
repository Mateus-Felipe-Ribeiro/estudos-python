# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("1º Número: "))
numero2 = int(input("2º Número: "))
numero3 = int(input("3º Número: "))

numerosOrdenados = sorted([numero1, numero2, numero3], reverse=True)

print("Os números em ordem decrescente são:",numerosOrdenados)

## Alternativa manual para 3 valores:
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
    if numero2 >= numero3:
        medio = numero2
        menor = numero3
    else:
        medio = numero3
        menor = numero2
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
    if numero1 >= numero3:
        medio = numero1
        menor = numero3
    else:
        medio = numero3
        menor = numero1
else:
    maior = numero3
    if numero1 >= numero2:
        medio = numero1
        menor = numero2
    else:
        medio = numero2
        menor = numero1

print("Os números em ordem decrescente são:", maior, medio, menor)

