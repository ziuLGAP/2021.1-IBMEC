"""
Exercicio 4-11
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
12/05/2021
"""

def saltos():
    """informa a média da distância dos saltos de um atleta"""
    distancias = []

    nome = input("Informe seu nome: ")
    for num in range(1, 6):
        dist = float(input(f"Informe a distância do salto de número {num}: "))
        distancias.append(dist)

    print(f"Atleta: {nome}")
    print("Primeiro salto:", distancias[0], "m")
    print("Segundo salto:", distancias[1], "m")
    print("Terceiro salto:", distancias[2], "m")
    print("Quarto salto:", distancias[3], "m")
    print("Quinto salto:", distancias[4], "m")

    print(f"Saltos: {distancias}")

    nova_lista = []
    nova_lista.extend(sorted(distancias))

    print(f"Melhor salto: {nova_lista[4]} m")
    nova_lista.pop(4)
    print(f"Pior salto: {nova_lista[0]} m")
    nova_lista.pop(0)
    media = sum(nova_lista) / len(nova_lista)
    print(f"Média dos saltos: {media} m")

    print("Resultado final:")
    print(f"{nome}: {media} m")

    return distancias
