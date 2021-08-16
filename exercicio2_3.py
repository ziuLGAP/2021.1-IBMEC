""""
Exercicio 2-3
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def informa_vogal_consoante(letra):
    """Informe uma letra e será dito se ela é uma vogal ou uma consoante"""
    if letra in ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u"):
        print(letra, "é uma vogal")
    else:
        print(letra, "é uma consoante")
