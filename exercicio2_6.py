"""
Exercicio 2-6
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""
def informa_maior_menor_numero(num1, num2, num3):
    """Informe 3 númueros e seá retornado o maior e menor deles"""
    if num1 > num2 and num1 > num3:
        print("O maior número é:", num1)
    elif num1 < num2 and num1 < num3:
        print("O menor número é:", num1)
    if num2 > num1 and num2 > num3:
        print("O maior número é:", num2)
    elif num2 < num1 and num2 < num3:
        print("O menor número é:", num2)
    if num3 > num1 and num3 > num2:
        print("O maior número é:", num3)
    elif num3 < num1 and num3 < num2:
        print("O menor número é:", num3)
