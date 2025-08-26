"""
 Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:


Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.


"""
# Dados da Viagem
distancia_percorrida = 300  # em km
combustivel_gasto = 25  # em litros

# Cálculo do Consumo Médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos Resultados
print(f"""
Distância Percorrida: {distancia_percorrida} km
Combustível Gasto: {combustivel_gasto} litros
Consumo Médio: {consumo_medio:.2f} km/l
""")

