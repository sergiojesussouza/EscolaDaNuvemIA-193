"""
Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 
caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma
válida seja inserida ou o usuário digite 'sair'.


"""
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário quer sair.
    if senha.lower() == "sair":
        print("Programa encerrado.")
        break
    
    # Verifica os critérios de senha forte.
    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue
    
    # Verifica se possui pelo menos um número
    if not any(caracter.isdigit() for caracter in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue    

    # Verifica se possui pelo menos uma letra.
    if not any(caracter.isalpha() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra.")
        continue    

    # Verifica se possui pelo menos uma letra maiúscula.
    if not any(caracter.isupper() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra Maiúscula.")
        continue    

     # Verifica se possui pelo menos um caracter especial.
    simbolos = "!@#$%^&*()-+?_=,<>/"
    if not any(caracter in simbolos for caracter in senha):
        print("Senha fraca: deve conter pelo menos um caracter especial Ex.: !@#$%^&* .")
        continue    


    # Se chegar até aqui, quer dizer que a senha é forte.   
    print("\nSenha forte e válida")
    break