# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

def ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

ano = int(input("Digite o ano: "))

if ano_bissexto(ano):
    print("o ano",ano, "é bissexto.")
else:
    print("o ano",ano, "não é bissexto.")