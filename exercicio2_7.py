"""
Exercicio 2-7
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def informa_menor_preco(prod1, prod2, prod3):
    """Informe o valor de 3 produtos e será mostrado o menor valor"""
    if prod1 < prod2 and prod1 < prod3:
        print("O melhor produto para se comprar é o de valor:", prod1)
    elif prod2 < prod1 and prod2 < prod3:
        print("O melhor produto para se comprar é o de valor:", prod2)
    elif prod3 < prod1 and prod3 < prod2:
        print("O melhor produto para se comprar é o de valor:", prod3)
informa_menor_preco(11.25, 11.50, 11)
