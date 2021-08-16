"""
Exercicio 2-14
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_media(ap1, a_cont):
    """Diz o quanto você precisa tirar na AP2 para não precisar fazer a AS,
     ou informa que será necessário fazer a AS."""
    ap2 = (7 - ap1 * 0.4 - a_cont * 0.2) / 0.4
    if ap2 > 10.0:
        print("Você precisa tirar mais de 10 na AP2. Será necessário fazer a AS.")
    else:
        print("Não será necessário fazer a AS se você tirar :", ap2, "ou mais na ap2.")
calcula_media(7, 8.8)