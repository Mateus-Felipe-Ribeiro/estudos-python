# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
import sys

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b','c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

entrada = input("Digite uma letra: ")

if len(entrada) > 1:
    print("entrada inválida!")
    sys.exit()

if entrada in vogais:
    print("Vogal")
elif entrada in consoantes:
    print("Consoante")
else:
    print("entrada inválida!")
    sys.exit()