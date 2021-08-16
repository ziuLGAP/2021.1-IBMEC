"""
Exercicio 2-12
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def exibe_dia(num):
    """Informa o dia da semana de acordo com o número selecionado"""
    if 1 <= num <= 7:
        if num == 1:
            print("Domingo")
        if num == 2:
            print("Segunda")
        if num == 3:
            print("Terça")
        if num == 4:
            print("Quarta")
        if num == 5:
            print("Quinta")
        if num == 6:
            print("Sexta")
        if num == 7:
            print("Sábado")
    else:
        print("Informe um valor entre 1 e 7.")
