# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

def verifica_numero(numero):
    if numero == round(numero):
        print("O número é inteiro.")
    else:
        print("O número é decimal.")

numero = float(input("Informe um número: "))
verifica_numero(numero)