"""
Exercicio 2-4
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_media(ap1, ap2, a_cont):
    """Informe as notas e será enviado se você foi ou não aprovado"""
    media = round(((ap1 + ap2) * 0.4 + a_cont * 0.2), 1)
    if 10 > media >= 7.0:
        print("Aprovado!")
    elif 7 > media > 0:
        print("Reprovado!")
    elif media == 10.0:
        print("Aprovado com Distinção!")
    elif media < 0.0:
        print("Nota inválida!")
    return media
