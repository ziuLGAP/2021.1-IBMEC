"""
Exercicio 2-9
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calucula_aumento(salario):
    "Informa o aumento do salário e outras informações"
    print("Salário antes do ajuste: R$", salario)
    if salario <=  280.00:
        print("O percentual de aumento aplicado é de: 20%")
        print("O valor do aumento é de: R$", salario * 0.2)
        print("O novo salário é de: R$", salario * 1.2)
    elif 280.00 < salario < 700.00:
        print("O percentual de aumento aplicado é de: 15%")
        print("O valor do aumento é de: R$", salario * 0.15)
        print("O novo salário é de: R$", salario * 1.15)
    elif 700.00 <= salario < 1500.00:
        print("O percentual de aumento aplicado é de: 10%")
        print("O valor do aumento é de: R$", salario * 0.10)
        print("O novo salário é de: R$", salario * 1.10)
    elif salario >= 1500.00:
        print("O percentual de aumento aplicado é de: 5%")
        print("O valor do aumento é de: R$", salario * 0.05)
        print("O novo salário é de: R$", salario * 1.05)
