# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def calcular_conceito_e_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 9.0 and media <= 10.0:
        conceito = "A"
        situacao = "APROVADO"
    elif media >= 7.5 and media < 9.0:
        conceito = "B"
        situacao = "APROVADO"
    elif media >= 6.0 and media < 7.5:
        conceito = "C"
        situacao = "APROVADO"
    elif media >= 4.0 and media < 6.0:
        conceito = "D"
        situacao = "REPROVADO"
    elif media >= 0.0 and media < 4.0:
        conceito = "E"
        situacao = "REPROVADO"
    else:
        conceito = "Inválido"
        situacao = "Inválido"

    return media, conceito, situacao

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media, conceito, situacao = calcular_conceito_e_aprovacao(nota1, nota2)

print("Notas: ", nota1, " e ", nota2)
print("Média: ", media)
print("Conceito: ", conceito)
print("Situação: ", situacao)

