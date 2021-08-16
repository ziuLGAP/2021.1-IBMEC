def peixes(peso):
    if peso -  50 > 0:
        excesso = peso - 50
        multa = excesso * 4.0
        print("Peso total de peixes (kg):", peso)   
        print("A quantidade de quilos excedente é de:", excesso)
        print("O valor da multa é de R$", multa)
        return multa
    else:
        print("Não há excesso")
peixes(50)