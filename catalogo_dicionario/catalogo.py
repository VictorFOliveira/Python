# declaração dos dicionários
catalogo_frutas = {}
catalogo_legumes = {}
catalogo_carnes ={}
# loop para iteração

while True:
    cadastro = input('Iniciar cadastro? Press (c) - finalizar cadastro Press (f): ')
    # Se usuário digitar (C) vai para o cadastro. (F) para finalização e visualização dos catalogos
    # Caso não escolher uma opção viavél cai no Else.

    if cadastro.lower() == 'c':
        secao = input('Qual seção deseja realizar cadastro? - frutas - legumes - carnes: ')
        # if para escolher a seção do cadastro
        if secao.lower() == 'frutas':
            print('seção de frutas')
            nome = input('Nome do produto: ')
            preco = float(input('preço do produto por kg: '))
            id = input('codigo ID: ')
            # O programa adiciona sem sobescrever os itens anteriores, usando o [id] como chave. Equivalente ao codigo do produto

            catalogo_frutas[id] ={'nome': nome,
                                  'preco': preco}
        
        elif secao.lower() == 'legumes':
            print('seção legumes')
            nome = input('Nome do produto: ')
            preco = float(input('Preco do produto: '))
            id = input('codigo ID: ')

            catalogo_legumes[id] ={'nome': nome,
                               'preco':preco}
            
        elif secao.lower() == 'carnes':
            print('seção de carnes')
            nome = input('Nome do produto: ')
            preco = float('Preço do produto: ')
            id = input('codigo ID: ')

            catalogo_carnes[id] = {'nome': nome,
                                   'preco': preco}
            

        else:
            print('opção invalida')

    elif cadastro =='f':
        break

    else:
        print('Opção invalida')


while True: 
    visualizar = input('Deseja visualizar um catalogo? Digite o nome do catalogo ou pressione (s) para sair.')

    if visualizar.lower() == 'catalogo frutas' or visualizar.lower() == 'frutas' or visualizar.lower() == 'catalogofrutas':
        if len(catalogo_frutas) == 0:
            print()
            print('Catalogo vazio')
            print('Nenhum produto cadastrado')

        else:

            print('----------------- Catalogo de Frutas -----------------')
        for key, value in catalogo_frutas.items():
            print(key, value)
        
        

    elif visualizar.lower() == 'catalogo legumes' or visualizar.lower() == 'legumes' or visualizar.lower() == 'catalogolegumes':
        if len(catalogo_legumes) == 0:
            print()
            print('Catalogo vazio')
            print('Nenhum produto cadastrado')

        else:

            print('----------------- Catalogo de Legumes -----------------')
        for key, value in catalogo_legumes.items():
            print(key, value)


    elif visualizar.lower() == 'catalogo carnes' or visualizar.lower() == 'carnes' or visualizar.lower() == 'catalogocarnes':
        if len(catalogo_carnes) ==0:
            print()
            print('Catalogo vazio')
            print('Nenhum produto cadastrado')
        
        else:

            print('----------------- Catalogo de Carnes -----------------')
        for key, value in catalogo_carnes.items():
            print(key, value)


    elif visualizar.lower() == 's':
        print('Cadastro de catalogo finalizado.')
        break

    else: 
        print('opção invalida')