def cabecalho(largura, titulo):
    print("=" * largura)
    
    if (largura - len(titulo)) % 2 == 1:
        print((" " + titulo).center(largura))
    else:
        print(titulo.center(largura))

    print("=" * largura)

cabecalho(40, "RELATÓRIO DE PAGAMENTO")