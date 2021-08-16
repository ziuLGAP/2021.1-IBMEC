"""
Exercicio 2-11
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_preco(area):
    ltr = area / 6
    print("A quantidade de tinta a ser comprada será de :", ltr, "litros")
    qntd1 = ltr / 18 
    qntd2 = ltr / 3.6
    if qntd1 >= 1:
        print("Se for comprar a tinta em latas, serão necessárias", qntd1, "lata(s) e isto custará: R$", qntd1 * 80)
    if qntd2 >= 1:
        print("Se for comprar a tinta em galões, serão necessários", qntd2, "galão(s) e isto custará: R$", qntd2 * 25)
    elif qntd1 >= 1 and qntd2 >= 1:
        print("Se for comprar tinta em latas e galões, serão necessários")