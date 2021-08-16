"""
Exercicio 4-4
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def le_consoantes():
    caracteres = []
    for _ in range(10):
        char = input("Informe uma letra: ")
    
        if char not in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
            caracteres.append(char)
    
    caracteres.sort()
    print(caracteres, len(caracteres))

le_consoantes()