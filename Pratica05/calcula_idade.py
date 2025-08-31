"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

"""

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade * 365  # Aproximação, sem considerar anos bissextos

# Programa principal
ano = int(input("Digite o ano de nascimento: "))
dias = idade_em_dias(ano)
print(f"Sua idade aproximada em dias é: {dias} dias.")