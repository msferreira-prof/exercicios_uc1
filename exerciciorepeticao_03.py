"""
Construa um algoritmo que, para um grupo de cinqüenta valores inteiros, 
determine: 
a) A soma dos valores positivos; 
b) A quantidade de valores negativos.
"""

soma_positivos = 0
quantidade_negativos = 0

for i in range(5):

    # entrada de dados
    numero_inteiro = int(input("Informe um numero: "))

    # processamento - soma dos valores positivos
    if numero_inteiro >= 0:
        soma_positivos = soma_positivos + numero_inteiro
    else: 
        quantidade_negativos = quantidade_negativos + 1

# saida de dados
print("A soma dos valores positivos é {0}".format(soma_positivos))
print( f"A quantidade de valores negativos é {quantidade_negativos}" )
