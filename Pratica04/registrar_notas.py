"""
Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve
continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. 
O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média 
da turma.


"""

notas = []

while True: # Manter o programa funcionando até o usuário digite fim
    try:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ")
        
        if entrada.lower() == 'fim':
            break
        
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            notas.append(nota) # adicinar à lista
        else:
            print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
            continue

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido ou 'fim' para encerrar.")
        
if notas:
    media = sum(notas) / len(notas)
    print(f"\nA média da turma: {media:.2f}")
    print(f"Total de Notas válidas registradas: {len(notas)}")
else:
    print("\nNenhuma nota válida foi registrada.")

