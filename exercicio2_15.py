"""
Exercicio 2-15
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
Data: 09/04/2021
"""

def informa_triangulo(lado1, lado2, lado3):
    """Informa se é um triângulo e o tipo de triângulo."""

    if lado3 - lado2 < lado1 < lado2 + lado3 and \
        lado3 - lado1 < lado2 < lado1 + lado3 and \
        lado2 - lado1 < lado3 < lado1 + lado2:

        if lado1 == lado2 and lado1 == lado3:

            print("É um triângulo equilátero.")

        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:

            print("É um triângulo isósceles.")

        elif lado1 != (lado2, lado3) and lado2 != lado3:

            print("É um triângulo escaleno.")

        return True

    print("Esses valores não formam um triângulo.")

    return False
