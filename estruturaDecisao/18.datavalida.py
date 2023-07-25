# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def data_valida(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia > 29:
                    return False
            elif dia > 28:
                return False
        return True
    except:
        return False

data = input("Insira a data (dd/mm/yyyy): ")

if data_valida(data):
    print(data, "é uma data válida.")
else:
    print(data, "não é uma data válida.")