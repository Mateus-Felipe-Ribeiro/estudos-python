# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Insira a altura: "))

pesoIdealHomem = (72.7*altura)-58
pesoIdealMulher = (62.1*altura)-44.7
print("Para homens", pesoIdealHomem)
print("Para mulheres", pesoIdealMulher)