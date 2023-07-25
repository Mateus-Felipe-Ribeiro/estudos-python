# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Valor 1º produto: R$"))
produto2 = float(input("Valor 2º produto: R$"))
produto3 = float(input("Valor 3º produto: R$"))

menor = min(produto1,produto2,produto3)

print("O produto com menor valor é o de R$",menor)