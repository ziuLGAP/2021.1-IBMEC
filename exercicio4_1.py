"""
Exercicio 4-1
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def le_cinco_numeros():
    """Lê cinco números inteiros e exibe na tela."""
    numeros = []
    for _ in range(5):
        numeros.append(int(input("Informe um número: ")))

    print(numeros)

le_cinco_numeros()