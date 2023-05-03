lista_de_compras = []
compra = True
while compra:
    escolha = input('Deseja adicionar itens?[i]. Deseja apagar itens[a]. Deseja listar itens?[l]. Finalizar a lista[f]: ')

    if escolha == 'i' or escolha == 'I':
        produto = input('Digite o produto: ')
        lista_de_compras.append(produto)
        print(lista_de_compras)
        
    elif escolha == 'a' or escolha == 'A':
        indice = input('Qual item deseja excluir? Escolha o indice: ')
        del lista_de_compras[int(indice)]

    elif escolha == 'l' or escolha == 'L':
        for numero, item in enumerate(lista_de_compras):
            print(numero, item)
            continue
     
    elif escolha == 'f' or escolha == 'F':
        print('produtos escolhidos')
        for numero, item in enumerate(lista_de_compras):
            print(numero, item)
        break
