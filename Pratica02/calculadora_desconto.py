"""
Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:


Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


"""

nome_produto = "Camiseta" # strings
preco_original = 50.00  # float
porcentagem_desconto = 20  # Inteiro

valor_desconto = preco_original * (porcentagem_desconto) / 100
preco_final = preco_original - valor_desconto

print(f"""
Produto: {nome_produto}
Preço Original: R$ {preco_original:.2f}
Desconto: {porcentagem_desconto} % 
Valor de Desconto: R$ {valor_desconto:.2f}
Preço Final: R$ {preco_final:.2f}
""")
