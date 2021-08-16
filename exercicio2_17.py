"""
Exercicio 2-17
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
Data: 09/04/2021
"""

def determina_ano_bissexto():
    """Determina se o ano escolhido é ou não bissexto."""

    ano = int(input("Informe o ano: "))

    if ano % 4 == 0 and ano % 100 != 0:

        print("É um ano bissexto.")

        return True

    if ano % (4 and 100) == 0:

        if ano % 400 == 0:

            print("É um ano bissexto.")

            return True

        print("Não é um ano bissexto.")

        return False

    print("Não é um ano bissexto.")

    return False
