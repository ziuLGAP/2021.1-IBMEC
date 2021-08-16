"""
Exercicio 3-16
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""
"""
def calcula_fatorial(numero):
    Calcula o fatorial de um número
    produto = 1
    while numero > 1:
        produto = produto * numero
        numero -= 1
    print(produto)
    return produto
calcula_fatorial()
"""

def calcula_fatorial(valor):
    """ Retorna fatorial de um número"""
    prod = 1

    for num in range(1, valor + 1):
        prod *= num

        print(prod)
        return prod
calcula_fatorial(4)