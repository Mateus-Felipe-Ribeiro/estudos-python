# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

def calculo_loja_tintas(litro):
    # LATAS
    latas = litro / 18
    if latas % 18 != 0:
        latas += 1
    preco_das_latas= latas * 80

    # GALOES
    galoes = litro / 3.6
    if galoes % 3.6 != 0:
        galoes += 1
    preco_dos_galoes = galoes * 25

    mistura_lata = int(litro / 18.0)
    mistura_galao = int((litro - (mistura_lata * 18)) / 3.6)
    if litro - (mistura_lata * 18) % 3.6 != 0:
        mistura_galao += 1
    galoes_total = (mistura_lata * 80) + (mistura_galao * 25)


    print(f'''
        Total de Litros necessário para pintar: {litro:.0f}L
        Apenas latas de 18 litros: {latas:.0f} Und. - Preço: R$ {preco_das_latas:.2f}
        Apenas galões de 3.6 litros: {galoes:.0f} Und. - Preço: R$ {preco_dos_galoes:.2f}
        Mistura: {mistura_lata:.0f} Latas e {mistura_galao:.0f} Galões = 
        R$ {galoes_total:.2f}''')

area_pintura = float(input('Tamanho em metros quadrados da área a ser pintada: '))
litros = area_pintura / 6  * 1.1
calculo_loja_tintas(litros)