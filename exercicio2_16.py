"""
Exercicio 2-16
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_raizes(num_a, num_b, num_c):
    """Calcula as raízes de uma equação do segundo grau."""
    if num_a == 0:
        print("Não é uma equação do segundo grau.")
    delta = num_b ** 2 - 4 * num_a * num_c
    raiz1 = round((-num_b + delta **(1/2)) / 2 * num_a, 2)
    raiz2 = round((-num_b - delta **(1/2)) / 2 * num_a, 2)
    if delta < 0:
        print("Não existem raízes.")
    elif delta == 0:
        print("Existe apenas uma raiz, que é:", raiz1)
    elif delta > 0:
        print("Existem duas raízes, que são:", raiz1,  "e", raiz2)
calcula_raizes(1, 5 ,5)