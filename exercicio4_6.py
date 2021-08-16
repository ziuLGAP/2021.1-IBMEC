"""
Exercicio 4-6
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
12/05/2021
"""

def calcula_media():
    """Calcula a média de 4 notas de 10 alunos diferentes e retorna aqueles que obtiveram\
        média acima de 7.0"""

    media = []
    media_aprov = []

    for _ in range(10):
        for _ in range(4):
            notas = []
            notas.append(float(input("Informe sua nota: ")))

        media.append(sum(notas) / len(notas))
        if (sum(notas) / len(notas)) >= 7.0:
            media_aprov.append(sum(notas) / len(notas))


    print("Quantidade de pessoas que tiraram mais que 7.0:", len(media_aprov))

    return media
