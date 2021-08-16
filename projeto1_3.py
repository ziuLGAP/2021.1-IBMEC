"""
Projeto integrador: Programação
Pojeto 1.3 - Chute um número
Grupo:
Felipe Balsa Maia Telles - 202102326346
Luiz Guilherme de Andrade Pires - 202102623758
Maria Heloise Muniz da Silva - 202102292301
Matheus de Souza Jannotti de Oliveira - 202102307279
"""

import random

def valida_dados(info):
    """Irá validar os dados fornecidos pelo usuário"""

    if info.isnumeric():
        if int(info) <= 100:
            if int(info) > 0:

                return True

            print("Insira um valor maior que zero!")

            return False

        print("Insira um valor menor ou igual a 100!")

        return False

    print("Insira um valor válido")

    return False

def main():
    """Função principal que irá dizer se o usuário chutou alto ou baixo \
        até o usuário acertar o valor escolhido pelo programa."""

    numero = random.randint(1, 100)

    while True:

        chute = input("Chute um número entre 1 e 100 (ENTER para sair):")

        if chute == "":
            print("Fechando o programa...")

            return None

        if valida_dados(chute):

            if int(chute) < int(numero):
                 print("O chute foi muito baixo!")

            if int(chute) > int(numero):
                print("O chute foi muito alto!")

            if int(chute) == int(numero):
                print("Parabéns! Você acertou a resposta!")
                break
main()