# Faça um Programa que leia três números e mostre o maior deles.

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

numero1 = int(input("1º Número: "))
numero2 = int(input("2º Número: "))
numero3 = int(input("3º Número: "))

maiorNumero = find_largest(numero1,numero2,numero3)

maior = max(numero1, numero2, numero3)

print("O maior número entre",numero1,",",numero2,"e",numero3," é:",maiorNumero)
print("Usando função max o maior número é:",maior)