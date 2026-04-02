# Elabore um algoritmo que imprima todos os números pares 
# compreendidos entre 85 e 907. O algoritmo deve também calcular e mostrar a 
# soma desses valores.

soma = 0
for numero in range(85, 907):
    
    modulo_numero = numero % 2
    if modulo_numero == 0:
        print( f"O número [{numero}] é par." )
        soma = soma + numero

print( f"A soma dos número pares é {soma}" )




        
    
    


