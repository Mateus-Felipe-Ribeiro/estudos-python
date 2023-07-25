# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        # Salário Bruto: (5 * 220)        : R$ 1100,00
        # (-) IR (5%)                     : R$   55,00  
        # (-) INSS ( 10%)                 : R$  110,00
        # FGTS (11%)                      : R$  121,00
        # Total de descontos              : R$  165,00
        # Salário Liquido                 : R$  935,00

porHora = float(input("Insira quanto você ganha por hora: "))
horas = float(input("Insira quantas hora você trabalha por mês: "))
IR = 0.05
INSS = 0.10
FGTS = 0.11
Sindicato = 0.03
salarioBruto = porHora * horas

if salarioBruto <= 900:
    IR = 0
elif salarioBruto <= 1500:
    IR = 0.05
elif salarioBruto <= 2500:
    IR = 0.1
elif salarioBruto > 2500:
    IR = 0.2
    
IR = salarioBruto * IR
INSS = salarioBruto * INSS
FGTS = salarioBruto * FGTS
Sindicato = salarioBruto * Sindicato

totalDiscontos = IR + INSS + Sindicato

salarioLiquido = salarioBruto - totalDiscontos

print("Salário Bruto: (",porHora,"*",horas,")        : R$",salarioBruto)
print("(-) IR (",IR*100,")               : R$",IR)
print("(-) INSS (10%)                  : R$",INSS)
print(" FGTS (11%)                  : R$",FGTS)
print("(-) Sindicato (3%)              : R$",Sindicato)
print("Total de descontos              : R$",totalDiscontos)
print("Salário Liquido                 : R$",salarioLiquido)