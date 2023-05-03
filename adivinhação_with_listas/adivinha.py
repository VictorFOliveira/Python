import random 
palavras = ['maca','pera','uva','melancia']
palavra_surpresa = random.choice(palavras)
letras_acertadas = ''


print('----------------- palavra secreta -----------------')
while True:
    chute = input('Escolha uma letra para adivinhar a palavra secreta: ')
    if chute in palavra_surpresa:
        letras_acertadas += chute


    palavra_nova = ''
    for letra_secreta in palavra_surpresa:
        if letra_secreta in letras_acertadas:
            palavra_nova += letra_secreta
        
        else:
            palavra_nova += '*'

    print(palavra_nova)

    if palavra_nova == palavra_surpresa:
        print('Você acertou')
        break


