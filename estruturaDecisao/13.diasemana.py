# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite um número (1-7): "))

if dia == 1:
    print("Dia da semana: Domingo")
elif dia == 2:
    print("Dia da semana: Segunda")
elif dia == 3:
    print("Dia da semana: Terça")
elif dia == 4:
    print("Dia da semana: Quarta")
elif dia == 5:
    print("Dia da semana: Quinta")
elif dia == 6:
    print("Dia da semana: Sexta")
elif dia == 7:
    print("Dia da semana: Sábado")
else:
    print("Entrada inválida!")
