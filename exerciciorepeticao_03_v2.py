"""
Construa um algoritmo que, para um grupo de cinqüenta valores inteiros, 
determine: 
a) A soma dos valores positivos; 
b) A quantidade de valores negativos.
"""
# teste do github
soma_positivos = 0
quantidade_negativos = 0
lista_numeros = []

# entrada de dados
for i in range(5):
    numero_inteiro = int(input("Informe um numero: "))
    lista_numeros.append(numero_inteiro)

print(lista_numeros)    

# processamento - soma dos valores positivos
qtd_elementos_lista = len(lista_numeros)
for i in range(qtd_elementos_lista):
    numero_inteiro = lista_numeros[i]    
    
    if numero_inteiro >= 0:
        soma_positivos = soma_positivos + numero_inteiro
    else: 
        quantidade_negativos = quantidade_negativos + 1    

# saida de dados
print("A soma dos valores positivos é {0}".format(soma_positivos))
print( f"A quantidade de valores negativos é {quantidade_negativos}" )
