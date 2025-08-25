"""
Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 

O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

"""

# Variáveis com os detalhes do produto
nome_produto = "Cadeira Infantil" # String
preco_unitario = 12.40 # Float
quantidade = 3 # Inteiro

# Variável do Cálculo do valor total
preco_total = preco_unitario * quantidade # Cálculo do Preço Total  

# Print com o resultado do valor total (saída)
print(f"Produto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}") 
print(f"Quantidade: {quantidade}")
print(f"Preço Total: R$ {preco_total:.2f}")

