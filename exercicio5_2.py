"""
Exercicio 5-2
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
25/05/2021
"""
def valida_datas(data):
    """Valida as datas recebidas"""
    if (data[3] + data[4]).isnumeric():

        if (data[3] + data[4]) == ("01") or ("02") or ("03") or ("04") or ("05") or ("06")\
            or ("07") or ("08") or ("09") or ("10") or ("11") or ("12"):

            if (data[3] + data[4]) == "02":
                if 0 < int(data[0] + data[1]) < 29:

                    return True

            elif (data[3] + data[4]) == ("04") or ("06") or ("09") or ("11"):
                if 0 < int(data[0] + data[1]) < 31:

                    return True

            else:
                if 0 < int(data[0] + data[1]) < 32:

                    return True

        return None

    return None

def data_extenso():
    """Escreve a data informada pelo usuário por extenso"""
    meses = {
        "01": "Janeiro",
        "02": "Fevereiro",
        "03": "Março",
        "04": "Abril",
        "05": "Maio",
        "06": "Junho",
        "07": "Julho",
        "08": "Agosto",
        "09": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro"
    }
    while True:
        data = input("Informe da data (no formato DD/MM/AAAA): ")

        if len(data) == 10:
            if valida_datas(data):
                break

            print("Selecione um valor válido!")

        else:
            print("Use o formato DD/MM/AAAA!")

    print(data[0] + data[1], "de", meses[data[3] + data[4]], "de",\
 data[6] + data[7] + data[8] + data[9])

data_extenso()