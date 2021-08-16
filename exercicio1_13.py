"""
Exercício 13
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
15/03/2021
"""

def calcula_salario_liquido(dindin_hora, horas_trabalhadas):
    """Informe quanto você ganha p/hora e quantas horas trabalha p/mês
e será calculado o sálario líquido e outras informações"""
    salario_b = dindin_hora * horas_trabalhadas
    impr = salario_b * 0.11
    inss = salario_b * 0.08
    sind = salario_b * 0.05
    salario_l = salario_b - impr - inss - sind
    print("Seu salario bruto é de R$", salario_b)
    print("(-)O valor do Imposto de Renda: R$", impr)
    print("(-)O valor do INSS: R$", inss)
    print("(-)O valor do Sindicato: R$", sind)
    print("(=)Seu salario líquido é de R$", salario_l)
