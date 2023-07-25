# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
def palavra_plural(number, unit):
    if number == 1:
        return str(number) + " " + unit
    else:
        return str(number) + " " + unit + "s"

numero = int(input("Digite um valor inteiro menor que 1000: "))

if numero >= 1000:
    print("Valor inválido.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    result = []

    if centenas > 0:
        result.append(palavra_plural(centenas, "centena"))

    if dezenas > 0:
        result.append(palavra_plural(dezenas, "dezena"))

    if unidades > 0:
        result.append(palavra_plural(unidades, "unidade"))

    output = " e ".join(result)
    print(numero, "=", output)