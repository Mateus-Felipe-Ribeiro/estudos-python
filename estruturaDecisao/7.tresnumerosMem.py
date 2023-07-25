# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input("1º Número: "))
numero2 = int(input("2º Número: "))
numero3 = int(input("3º Número: "))

maior = max(numero1,numero2,numero3)
menor = min(numero1,numero2,numero3)

print("Maior número:",maior)
print("Menor número:",menor)