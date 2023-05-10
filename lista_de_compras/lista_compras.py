# carrinho de compras 
product_list = []
purchase = True
total = 0.0

while purchase:
    print('------ carrinho de compras ------ ')
    option = input('press (B) to buy, press (F) to finalize, press (E) to erase: ')
        
    if option == 'b' or option == 'B':
        product = input('Which product do you want to add?: ')
        product_list.append(product)

        price = float(input('value of product: '))
        amount = float(input('How many:'))
        total_many = price*amount
        total += total_many
    

    elif option == 'f' or option == 'F':
        print(f'current price = {total}')
        for index, list in enumerate(product_list):
            print(index, list)
            break

    
    elif option == 'e' or option == 'E':
        indice = input('Qual indice deseja excluir: ')
        indice = int(indice)
        for index, list in enumerate(product_list):
            print(index, list)
        
        del product_list[indice]
        # reduzindo valor

        less_price = float(input('value of product: '))
        less_how = float(input('how many: '))

        less_total_many = less_price * less_how
        total  -=  less_total_many

    else: 
        print('digite uma opção valida')        
       

