# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def calcular_valor_a_pagar(morango, macas):
    preco_morango_ate_5kg = 2.50
    preco_morango_acima_5kg = 2.20
    preco_macas_ate_5kg = 1.80
    preco_macas_acima_5kg = 1.50
    
    if morango <= 5:
        valor_morango = morango * preco_morango_ate_5kg
    else:
        valor_morango = morango * preco_morango_acima_5kg
    
    if macas <= 5:
        valor_macas = macas * preco_macas_ate_5kg
    else:
        valor_macas = macas * preco_macas_acima_5kg
    
    valor_total = valor_morango + valor_macas
    
    if (morango + macas) > 8 or valor_total > 25:
        desconto = valor_total * 0.10
        valor_total -= desconto
    
    return valor_total

morango = float(input("Digite a quantidade de morangos (em Kg): "))
macas = float(input("Digite a quantidade de maçãs (em Kg): "))

valor_a_pagar = calcular_valor_a_pagar(morango, macas)
print("Valor a pagar: R$", valor_a_pagar)