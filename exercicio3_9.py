"""
Exercicio 3-9
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def informa_soma_media(limite):
    "Informa a soma e a média de cinco números"
    numeros_lidos = 0
    soma = 0

    while numeros_lidos < limite:
        num = input("Informe número: ")
        if num == "":
            print("Entrada inválida!")
        else:
            soma += float(num)
            numeros_lidos += 1

    media = soma / numeros_lidos
    print("A soma é",  soma)
    print("A média é", media)

    return media
informa_soma_media(6)