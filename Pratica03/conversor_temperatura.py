"""
Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.


"""

temperatura = float(input("Digite a temperatura que deseja converter (Ex. 36.5): "))    
origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

if origem == destino:
    resultado = temperatura

elif origem == "C": # Se origem for Celsius, então converter para Fahrenheit ou Kelvin
    if destino == "F":
        resultado = (temperatura * (9/5)) + 32 # Celsius para Fahrenheit
    else:
        resultado = temperatura + 273.15 # Celsius para Kelvin
    
elif origem == "F": # Se origem for Fahrenheit, então converter para Celsius ou Kelvin
    if destino == "C":
            resultado = (temperatura - 32) * (5/9) # Fahrenheit para Celsius
    else:
            resultado = (temperatura - 32) * (5/9) + 273.15 # Fahrenheit para Kelvin

else: # Se origem for Kelvin, então converter para Celsius ou Fahrenheit
     if destino == "C":
         resultado = temperatura - 273.15 # Kelvin para Celsius
     else:
        resultado = (temperatura - 273.15) * (9/5) + 32 # Kelvin para Fahrenheit

print(f"\n{temperatura} {origem} é igual a {resultado:.2f} {destino}")
