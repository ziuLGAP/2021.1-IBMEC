"""
Exercicio 4-3
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_media():
    notas = []
    for _ in range(4):
        notas.append(float(input("Informe uma nota: ")))

    print(notas)
    print("A média das notas é:", sum(notas) / len(notas))

calcula_media()