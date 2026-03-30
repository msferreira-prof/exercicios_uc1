""""
Faça um algoritmo que leia quatro números informados pelo usuário e 
que depois imprima a média ponderada, sabendo-se que os pesos são 
respectivamente: 1, 2, 3 e 4
"""
peso_1 = 1
peso_2 = 2
peso_3 = 3
peso_4 = 4

numero_1 = float(input("Informe o primeiro número: "))
numero_2 = float(input("Informe o segundo número: "))
numero_3 = float(input("Informe o terceiro número: "))
numero_4 = float(input("Informe o quarto número: "))    

soma_notas_x_peso = numero_1 * peso_1 + numero_2 * peso_2 + numero_3 * peso_3 + numero_4 * peso_4
soma_pesos = peso_1 + peso_2 + peso_3 + peso_4
media_ponderada = soma_notas_x_peso / soma_pesos

print(f"A Média ponderada para os números {numero_1:.2f}, {numero_2:.2f}, {numero_3:.2f} e {numero_4:.2f} informados é: {media_ponderada:.2f}")
print("A Média ponderada para os números " + numero_1 + ", " + numero_2 + ", " + numero_3 + " e " + numero_4 + " informados é: " + str(media_ponderada))

