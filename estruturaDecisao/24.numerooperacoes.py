# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

def verifica_propriedades(numero):
    propriedades = []

    if numero % 2 == 0:
        propriedades.append("par")
    else:
        propriedades.append("ímpar")

    if numero >= 0:
        propriedades.append("positivo")
    else:
        propriedades.append("negativo")

    if numero == round(numero):
        propriedades.append("inteiro")
    else:
        propriedades.append("decimal")

    return propriedades

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operation = input("Informe a operação matemática que deseja realizar (+, -, *, /): ")

if operation == "+":
    resultado = numero1 + numero2
elif operation == "-":
    resultado = numero1 - numero2
elif operation == "*":
    resultado = numero1 * numero2
elif operation == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    exit()

propriedades_numero = verifica_propriedades(resultado)

print("Resultado:", resultado)
print("O número é", ", ".join(propriedades_numero) + ".")