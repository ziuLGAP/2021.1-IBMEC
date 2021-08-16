"""
Exercicio 3-2
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def cria_sequencia(numero, limite):
    while numero < limite:
        print(numero, end=" - ")
        numero += 2

    print(numero)
cria_sequencia(2, 14)    
