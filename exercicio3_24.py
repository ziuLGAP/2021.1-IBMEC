"""
Exercicio 3-24
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_media(qntd):
    soma = 0
    for _ in range(qntd):
        soma += float(input("Informe uma nota: "))
    
    print(soma / qntd)

calcula_media(5)

