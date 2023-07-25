# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite (M) - Masculino ou (F) - Feminino: ")

if(letra.upper() == 'M'):
    print("M - Masculino")
elif(letra.upper() == 'F'):
    print("F - Feminino")
else:
    print("Eita bixo sapecagens!")