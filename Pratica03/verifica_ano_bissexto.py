"""
Verificador de Ano Bissexto


Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.



"""

ano = int(input("Digite um ano: ")) 

if ano % 4 == 0: # Se o ano for divisível por 4, ele poderá ser bissexto
    if ano % 100 == 0: # Se o ano for divisível por 100, precisa ser analisado 
        if ano % 400 == 0: # Se o ano for divisível por 400, então ele é bissexto
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    else:
        print(f"{ano} é um ano bissexto.") 
else:
    print(f"{ano} não é um ano bissexto.") 

