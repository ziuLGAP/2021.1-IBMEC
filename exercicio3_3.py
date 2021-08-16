"""
Exercicio 3-3
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def pede_senha():
    """Pede um nome e uma senha sendo que eles não podem ser iguais"""
    while True:
        nome = input("Informe seu nome: ")
        senha = input("Informe a senha: ")
        if nome != senha:
            break
        elif nome == senha:
            print("Não use como senha o seu nome!")
pede_senha()
