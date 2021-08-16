"""
Exercicio 3-20
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def determina_primo(valor):
    for num in range(2, valor + 1):
        if valor == 2:
            print(True)

        elif valor % num == 0:
            print(False)

        print(True)
        
        
determina_primo(2)