# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

def interrogatorio():
    respostas_positivas = 0
    
    pergunta1 = input("Telefonou para a vítima? (sim/não) ")
    if pergunta1.lower() == "sim":
        respostas_positivas += 1
    
    pergunta2 = input("Esteve no local do crime? (sim/não) ")
    if pergunta2.lower() == "sim":
        respostas_positivas += 1
    
    pergunta3 = input("Mora perto da vítima? (sim/não) ")
    if pergunta3.lower() == "sim":
        respostas_positivas += 1
    
    pergunta4 = input("Devia para a vítima? (sim/não) ")
    if pergunta4.lower() == "sim":
        respostas_positivas += 1
    
    pergunta5 = input("Já trabalhou com a vítima? (sim/não) ")
    if pergunta5.lower() == "sim":
        respostas_positivas += 1
    
    if respostas_positivas == 5:
        return "Assassino"
    elif respostas_positivas >= 3:
        return "Cúmplice"
    elif respostas_positivas >= 2:
        return "Suspeita"
    else:
        return "Inocente"

resultado = interrogatorio()
print("Classificação:", resultado)