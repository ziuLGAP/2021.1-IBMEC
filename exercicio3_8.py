"""
Exercicio 3-8
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def informa_maior_numero():
    """Lê cinco números e imprime o maior deles."""
    maior_numero = float("-inf")
    numeros_lidos = 0

    while numeros_lidos < 5:
        num = float(input("Informe um número: "))
        if num > maior_numero:
            maior_numero = num

        numeros_lidos += 1
    print("O maior número é", maior_numero)
    return maior_numero
