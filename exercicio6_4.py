def compara_string(txt1, txt2):
    print("String 1:", txt1)
    print("String 2:", txt2)

    print(f"Tamanho de \"{txt1}\":", len(txt1))
    print(f"Tamanho de \"{txt2}\":", len(txt2))

    if len(txt1) == len(txt2):
        print("As duas strings são do mesmo tamanho.")
    else:
        print("As duas stings são de tamanhos diferentes.")

    if txt1 == txt2:
        print("As duas strings possuem o mesmo conteúdo.")
    else:
        print("As duas strings possuem conteúdo diferente.")  

compara_string("Oi, mundo!","Oi, mundo!")  
