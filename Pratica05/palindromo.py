"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para 
frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for 
False, responda “Não”.


"""

def is_palindrome(texto):
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum()
                          )
    return texto_limpo == texto_limpo [::-1]

frase = input("Digite uma palavra ou Expressão: ")
resultado = is_palindrome(frase)

if resultado:
   resposta = "Sim"
else:
    resposta = "Não"

print(f"A frase '{frase}' é um palíndromo? {resposta}") 