"""

Calculadora de Número Inteiro

Leia quatro valores inteiros A, B, C e D. 

A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: 

DIFERENCA = (A * B - C * D).

Entrada: O arquivo de entrada contém 4 valores inteiros. 

Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

"""

valor_A = int(input("Digite o valor A: ")) 
valor_B = int(input("Digite o valor B: "))
valor_C = int(input("Digite o valor C: "))
valor_D = int(input("Digite o valor D: "))

diferenca = (valor_A * valor_B) - (valor_C * valor_D)

print("\nA fórmula é: DIFERENCA = (A * B) - (C * D).")
print(f"Substituindo a fórmula: ({valor_A} * {valor_B}) - ({valor_C} * {valor_D}).")
print(f"O resultado da diferença é DIFERENCA = {diferenca}.")   