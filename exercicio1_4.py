"""
Exercício 4
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
15/03/2021
"""

def calcula_media(ap1, ap2, a_cont):
    """Informe as notas na respectiva ordem: AP1, AP2 E AC
    e será enviado a sua média e também se foi aprovado"""
    media = round(((ap1 + ap2) * 0.4 + a_cont * 0.2), 1)
    print("Sua nota final será: ", media)
    if media >= 7.0:
        print("Parabéns, você foi aprovado!!!")
    else:
        print("Infelizmente você não foi aprovado, melhor estudar mais!!!")
calcula_media(9.3, 8.8, 10)