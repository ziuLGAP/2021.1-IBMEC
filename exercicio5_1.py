"""
Exercicio 5-1
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
24/05/2021
"""

def valida_dados(info):
    """Irá validar os dados informados pelo usuário"""
    if info.isnumeric():
        if 0 < int(info) <= 23:
            return True
        print("Informe um valor que esteja entre 1 e 23!")
        return False

    print("Informe um valor válido!")
    return False

def melhor_jogador():
    """Cria uma enquete, computa os votos e retorna o melhor jogador"""
    votos = []
    valor = 0
    valorj = 0
    mvp = ""

    print("Enquete: quem foi o melhor jogador ?")

    while True:
        voto = input("Informe do número do jogador que deseja votar(0 == fim): ")

        if valida_dados(voto):
            votos.append(int(voto))

        if voto == "0":
            print("Encerrando a enquete...")
            break

    print("Resultado da votação:")
    print(f"Foram computados {len(votos)} votos.")

    print("Jogador", "Votos".center(20), "%")

    votos_novo = sorted(votos)
    total = len(votos_novo)

    while valor < len(votos_novo):
        print(votos_novo[valor], " " * 13, (votos_novo.count(votos_novo[valor])),\
         " " * 10, (((votos_novo.count(votos_novo[valor])) / total) * 100), "%")

        if (votos_novo.count(votos_novo[valor])) > valorj:
            valorj = votos_novo.count(votos_novo[valor])
            mvp = votos_novo[valor]

        valor += votos_novo.count(votos_novo[valor])
    print(f"O melhor jogador foi o camisa {mvp}, com {valorj} votos,\
 correspondendo a {(valorj / total) * 100}% do total de votos.")
