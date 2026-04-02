# Elabore um algoritmo que imprima todos os números pares 
# compreendidos entre 85 e 907. O algoritmo deve também calcular e mostrar a 
# soma desses valores.

soma = 0
numeros_par = []

for numero in range(85, 907):
    modulo_numero = numero % 2
    if modulo_numero == 0:
        numeros_par.append(numero)
        soma = soma + numero

print( f"Lista de número pares: {numeros_par} ")

# 2a. forma
for numero_par in numeros_par:
    print( f"O número [{numero_par}] é par." )

# 3a. forma
tamanho_lista_pares = len(numeros_par)
for posicao_elemento in range(tamanho_lista_pares):
    numero_par = numeros_par[posicao_elemento]
    print( f"O número [{numero_par}] é par." )
   
# soma
print( f"A soma dos número pares é {soma}" )






        
    
    


