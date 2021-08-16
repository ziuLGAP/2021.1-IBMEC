"""
Exercicio 2-18
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_qntd_notas():
    """Informa a quantidade de notas de cada valor que será sacado."""
    dindin = int(input("Quanto deseja sacar?: "))
    if 10 <= dindin <= 600:
        qntd1 = dindin // 100
        qntd2 = (dindin - 100 * qntd1) // 50
        qntd3 = (dindin - 100 * qntd1 - 50 * qntd2) // 10
        qntd4 = (dindin - 100 * qntd1 - 50 * qntd2 - 10 * qntd3) // 5
        qntd5 = (dindin - 100 * qntd1 - 50 * qntd2 - 10 * qntd3 - 5 * qntd4) // 1
        dindin = qntd1 * 100 + qntd2 * 50 + qntd3 * 10 + qntd4 * 5 + qntd5 * 1
        print("Serão necessárias", qntd1, "notas de 100,", qntd2, "notas de 50,",\
 qntd3, "notas de 10,", qntd4,  "notas de 5 e", qntd5, "notas de 1.")
    else:
        print("Selecione um valor entre 10 e 600 reais.")
