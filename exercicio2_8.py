"""
Exercicio 2-8
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def saudacoes():
    """Responde de acordo com a informação que você eviou"""
    var =  input("Informe o turno em que você estuda: 'M' para matutino,\
    'V' para vespertino e 'N' para noturno:")
    if var in ("M", "m"):
        print("Bom Dia!")
    elif var in ("V", "v"):
        print("Boa Tarde!")
    elif var in ("N", "n"):
        print("Boa Noite!")
    else:
        print("Valor Inválido!")
saudacoes()
