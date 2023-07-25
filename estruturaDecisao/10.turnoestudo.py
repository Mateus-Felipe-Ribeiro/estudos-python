# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Em que turno você estuda? (M - matutino)(V - vespertino)(N - noturno) : ")

if(turno.upper() == 'M'):
    print("Bom dia!")
elif turno.upper() == 'V':
    print("Boa tarde!")
elif turno.upper() == 'N':
    print("Boa noite!")
else:
    print("Valor inválido!")