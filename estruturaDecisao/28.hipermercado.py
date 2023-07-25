# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_valor_a_pagar(tipo_carne, quantidade, cartao_tabajara):
    preco_file_duplo_ate_5kg = 4.90
    preco_file_duplo_acima_5kg = 5.80
    preco_alcatra_ate_5kg = 5.90
    preco_alcatra_acima_5kg = 6.80
    preco_picanha_ate_5kg = 6.90
    preco_picanha_acima_5kg = 7.80
    
    if tipo_carne == "File Duplo":
        if quantidade <= 5:
            valor_total = quantidade * preco_file_duplo_ate_5kg
        else:
            valor_total = quantidade * preco_file_duplo_acima_5kg
    elif tipo_carne == "Alcatra":
        if quantidade <= 5:
            valor_total = quantidade * preco_alcatra_ate_5kg
        else:
            valor_total = quantidade * preco_alcatra_acima_5kg
    elif tipo_carne == "Picanha":
        if quantidade <= 5:
            valor_total = quantidade * preco_picanha_ate_5kg
        else:
            valor_total = quantidade * preco_picanha_acima_5kg
    else:
        return "Tipo de carne inválido"
    
    if cartao_tabajara:
        desconto = valor_total * 0.05
        valor_total -= desconto
    
    return valor_total

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ")
quantidade = float(input("Digite a quantidade de carne (em Kg): "))
cartao_tabajara = input("A compra será feita com o cartão Tabajara? (S/N): ")

if cartao_tabajara.upper() == "S":
    cartao_tabajara = True
else:
    cartao_tabajara = False

valor_a_pagar = calcular_valor_a_pagar(tipo_carne, quantidade, cartao_tabajara)

print("Cupom Fiscal:")
print("Tipo de carne:", tipo_carne)
print("Quantidade:", quantidade, "Kg")
print("Preço total: R$", valor_a_pagar)

if cartao_tabajara:
    print("Tipo de pagamento: Cartão Tabajara")
    print("Valor do desconto: R$", valor_a_pagar * 0.05)
else:
    print("Tipo de pagamento: Outro")
    print("Valor do desconto: R$ 0.00")

print("Valor a pagar: R$", valor_a_pagar)