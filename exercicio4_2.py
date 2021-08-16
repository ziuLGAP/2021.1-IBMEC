"""
Exercicio 4-1
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def le_dez_numeros_contrario():
    numeros = []
    for _ in range(10):
        numeros.append(int(input("Informe um número  ")))

    print(numeros[::-1])

le_dez_numeros_contrario()