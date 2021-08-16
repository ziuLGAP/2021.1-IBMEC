"""
Exercicio 3-26
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
Data: 28/04/2021
"""

def votos(qntd):
    """Computa os votos dos usuários e informa a quantidade de votos de cada candidato"""
    cand1 = 0
    cand2 = 0
    cand3 = 0

    for _ in range(qntd):
        voto = input("Informe o Número do candidato no qual deseja votar(1 para o candidato 1,\
 2 para o canditado 2 e 3 para o candidato 3, caso seja inserido qualquer outro valor, o\
 voto não será computado):  ")

        if voto == "1":
            cand1 += 1

        elif voto == "2":
            cand2 += 1

        elif voto == "3":
            cand3 += 1

    print("O número de votos do candidato 1 foi :", cand1, "votos.")
    print("O número de votos do candidato 2 foi :", cand2, "votos.")
    print("O número de votos do candidato 3 foi :", cand3, "votos.")

    return cand1, cand2, cand3
