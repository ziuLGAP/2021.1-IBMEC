"""
Projeto integrador: Programação
Pojeto 1.1 - Simulador de Dados
Grupo:
Felipe Balsa Maia Telles - 202102326346
Luiz Guilherme de Andrade Pires - 202102623758
Maria Heloise Muniz da Silva - 202102292301
Matheus de Souza Jannotti de Oliveira - 202102307279
"""

import random

def rola_dados(dado, qtde):
    """Irá jogar uma quantidade [qtde] de dado(s) de [dado] lados."""

    rolagens = []

    for num in range(qtde):
        rolagens.append(str(random.randint(1, dado)))
        print("Lançamento n.", num + 1, "-", rolagens[-1])

    print(qtde, "dado(s) de", dado, "lados:")
    print(" ".join(rolagens))

def valida_dados(info):
    """Irá validar os dados informados pelo usuário"""

    if info.isnumeric():
        if int(info) <= 0:
            print("Insira um valor maior que zero!")
            return False

        return True

    print("Insira um valor válido!")
    return False

def main():
    """Função principal do simulador de dados."""

    while True:
        dado = input("Insira a quantidade de faces do dado(ENTER para sair): ")
        if dado == "":
            print("Fechando o programa...")
            break

        if valida_dados(dado):
            while True:
                qtde = input("Insira o número de vezes que deseja rolar o dado(ENTER == 1): ")

                if qtde == "":
                    qtde = "1"
                    rola_dados(int(dado), int(qtde))
                    return None

                if valida_dados(qtde):
                    rola_dados(int(dado), int(qtde))
                    return None
main()