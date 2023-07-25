# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Insira o salário do coloborador: R$"))

salarioReajustado = 0
valorAumento = 0

if salario <= 280.0:
    percentual = 0.2
elif salario <= 700.0:
    percentual = 0.15
elif salario <= 1500.0:
    percentual = 0.1
else:
    percentual = 0.05

valorAumento = salario * percentual
salarioReajustado = salario + valorAumento

print("Salario antes do reajuste: R$",salario)
print("Percentual de aumento:",percentual*100,"%")
print("Valor do aumento: R$",valorAumento)
print("Salario depois do reajuste: R$",salarioReajustado)