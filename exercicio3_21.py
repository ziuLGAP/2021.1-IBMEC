"""
Exercicio 3-21
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
Data: 09/04/2021
"""

def determina_primo(valor):
    """Determina se o valor é primo e informa seus divisores"""

    divisores = []

    for num in range(2, valor):
        if valor % num == 0:
            divisores.append(num)

    if divisores == []:

        print("É um número primo")

    if len(divisores) >= 1:

        print("Não é um número primo")

        print("todos os divisores(tirando 1 e o próprio valor):", divisores)
