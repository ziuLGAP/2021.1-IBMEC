"""
Exercicio 4-10
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
12/05/2021
"""

def mescla_listas():
    """Mescla as listas, intercalando seus elementos"""

    lista1 = []
    lista2 = []

    for _ in range(10):
        lista1.append(input("Informe um dos elemento da lista 1: "))
        lista2.append(input("Informe um dos elementos da lista 2: "))

    cont1 = 1

    for valor in range(10):
        lista1.insert(cont1, lista2[valor])
        cont1 += 2

    print(lista1)
    return lista1
