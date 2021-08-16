"""
Exercicio 3-1
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def pede_nota():
    """Pede uma nota entre 0 e 10."""
    while True:
        numero = float(input("Informe uma nota: "))
        if 0 <= numero <= 10:
            print("Obrigado pelo feedback!")
            break
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
pede_nota()