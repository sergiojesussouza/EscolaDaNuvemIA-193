"""
Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:



Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.


"""

valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# taxa do dolar === Preciso de R$ 5.60 para comprar 1 dolar

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print(f"valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: U$$ {valor_dolares:.2f}")
print(f"Valor em Euros: € {valor_euros:.2f}")


