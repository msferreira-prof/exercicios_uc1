
lista_cliente = []
lista_valor_compra = []
lista_desconto = []
lista_valor_pagar = []
total_arrecadado_loja = 0

# entrada de dados
qtdClientes = int(input("Informe a quantidade de clientes que efetuaram compras na loja: "))

for i in range(qtdClientes):
    nome_cliente = input( f"Informe o nome do {i+1}o. cliente: " )
    valor_compra = float(input( f"Informe o valor da compra do {i+1}o. cliente: " ))
    
    lista_cliente.append(nome_cliente)
    lista_valor_compra.append(valor_compra)

# processamento
for i in range(qtdClientes):
    valor_compra = lista_valor_compra[i]
    if valor_compra >= 250.0:
        taxa_desconto = 20/100
    else:   
        taxa_desconto = 15/100

    desconto = valor_compra * taxa_desconto
    valor_pagar = valor_compra - desconto
    # valor_pagar = valor_compra * (1.0 - taxa_desconto)
    
    lista_desconto.append(desconto)
    lista_valor_pagar.append(valor_pagar)
    
for i in range(qtdClientes):
    print( f'O cliente "{lista_cliente[i]}" comprou R$ {lista_valor_compra[i]:.2f}, recebeu de desconto R$ {lista_desconto[i]:.2f}, totalizando R$ {lista_valor_pagar[i]:.2f} a pagar')
    total_arrecadado_loja += lista_valor_pagar[i]    

# saida de dados
print( f"A loja arrecadou R$ {total_arrecadado_loja:.2f}" )
