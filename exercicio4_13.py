
carros = ["UNO", "GOL", "FUSCA", "VECTRA", "CHEVETTE"]

consumo = ["12.5", "10", "7", "9", "5"]
"""
def compara_carros(carro, km_l):
    for num in range(len(carro)):
        print("Veículo", num + 1)
        print("Nome:", carro[num])
        print("Km por litro:", km_l[num])

    

    for num1 in range(len(carro)):
        litro = 1000 / float(km_l[num1])
        custo = litro * 2.25
        print(num1 + 1, "-", carro[num1], "-", km_l[num1], "-", litro, "litros -", "R$", custo)

compara_carros(carros, consumo)
"""

def carros_lista(carros):

    print("Comparatativo de consumo de combustivel")

    ef_max = 0
    carro_economico = ""
    cont = 1

    for modelo, eficiencia in carros.items():
        print("Veículo", cont)
        print("Nome:", modelo)
        print("Km por litro:", eficiencia)

        cont += 1

        if eficiencia > ef_max:
            ef_max = eficiencia
            carro_economico = modelo

    cont = 1

    print("\nRelatório final\n")
    for modelo, eficiencia in carros.items():
        print(
            cont,
            modelo,
            eficiencia,
            str(1000 / eficiencia) + "litros",
            "R$ " + str(2.25 * 1000 / eficiencia),
            sep=" - " 
        )

        cont += 1

    print("O menor consumo é do", carro_economico)

carros = {
    "UNO": 12.5,
    "Gol": 10,
    "Fusca": 7,
    "Vectra": 9,
    "Chevette": 5
}

carros_lista(carros)