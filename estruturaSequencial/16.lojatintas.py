# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = float(input("Quantos metros quadrados serão pintados? "))
coberturaLitros = 1 
coberturaMetros = 3
tamanhoLataLitros = 18
valorLataReais = 80.00
litrosGastos = (metros/coberturaMetros)
print("litros gastos", litrosGastos)
if(litrosGastos > 1):
    quantidadeLatas = round((litrosGastos/tamanhoLataLitros))
    precoTotal = quantidadeLatas * valorLataReais
else:
    quantidadeLatas = 1
    precoTotal = valorLataReais
print("Quantidade de latas necessárias:",quantidadeLatas)
print("Valor total: R$",precoTotal)