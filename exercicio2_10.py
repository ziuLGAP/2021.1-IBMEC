"""
Exercicio 2-10
Luiz Guilherme de Andrade Pires
Engenharia de Computação
Matrícula: 202102623758
"""

def calcula_salario_liquido(dindin_hora, horas_trabalhadas):
    """Informe quanto você ganha p/hora e quantas horas trabalha p/mês
e será calculado o sálario líquido e outras informações"""
    salario_b = dindin_hora * horas_trabalhadas
    sind = salario_b * 0.03
    if salario_b <= 900.00:
        impr = 0
    elif 900.00 < salario_b <= 1500.00:
        impr = salario_b * 0.05
    elif 1500.00 < salario_b <= 2500.00:
        impr = salario_b * 0.1
    elif salario_b > 2500.00:
        impr = salario_b * 0.2
    salario_l = salario_b - sind - impr
    fgts = salario_b * 0.11
    print("Seu salario bruto é de R$", salario_b, ".")
    print("(-)O valor do Imposto de Renda: R$", impr, ".")
    print("(-)O valor do FGTS: R$", fgts, "que será pago pela empresa.")
    print("(-)O valor do Sindicato: R$", sind, ".")
    print("(=)Seu salario líquido é de R$", salario_l, ".")
