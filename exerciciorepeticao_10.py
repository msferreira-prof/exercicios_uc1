"""
nome da praia
a sua distância do centro da cidade 
o número médio de veranistas da última temporada 
tipo de acesso à praia (0 - acesso não asfaltado; 1 - acesso asfaltado)

{ "barra da tijuca": [20.0, 1000.0, 1.0], "botafogo": [1.0, 1.0, 1.0], .... }


"""
praias = {}
continua = 0

while continua == 0:
    # receber informacoes da praia
    nome_praia = input("Informe o nome da praia: ")
    distancia_centro = float(input("Informe a distância da praia ao centro da cidade em Km: "))
    media_veranistas = float(input("Informe o número médio de veranistas na praia: "))
    tipo_acesso = float(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado; 1 - acesso asfaltado): "))
    
    # inserindo no dicionario o nome da praia como Key/Chave e lista de dados como Value/Valor
    praias[nome_praia] = [distancia_centro, media_veranistas, tipo_acesso]
    
    # pergunto se deseja continua e cadastrar uma nova praia
    continua = int(input("\nDeseja cadastrar nova praia (0 - Sim / Qualquer outro número - Não): "))
    print()
                        
# processamento
numero_praias_15km = 0
numero_veranistas_praia_nao_asfaltada = 0
praias_acesso_asfaltado_menos_1000_veranistas = {}
media_veranistas = 0
quantidade_praias_acesso_nao_asfaltado = 0

nomes_praia = praias.keys()
for nome in nomes_praia:
    elemento = praias.get(nome)
    print(elemento)
   
    distancia_centro = elemento[0]
    numero_veranistas = elemento[1]
    tipo_acesso = elemento[2]
    
    if distancia_centro > 15:
        numero_praias_15km = numero_praias_15km + 1
    
    if tipo_acesso == 0:
        numero_veranistas_praia_nao_asfaltada = numero_veranistas_praia_nao_asfaltada + numero_veranistas
        quantidade_praias_acesso_nao_asfaltado = quantidade_praias_acesso_nao_asfaltado + 1
    
    ##  O nome e a distância do centro, em km, de todas as praias de acesso 
    ##  asfaltado que tiveram menos de 1000 veranistas. 
    if tipo_acesso == 1 and numero_veranistas < 1000:
        praias_acesso_asfaltado_menos_1000_veranistas[nome] = distancia_centro

if quantidade_praias_acesso_nao_asfaltado > 0:         
    media_veranistas = numero_veranistas_praia_nao_asfaltada / quantidade_praias_acesso_nao_asfaltado
    
# saida
print( f"Número de praias mais de 15 km do centro: {numero_praias_15km} ")
print( f"Média de veranistas de praias com acesso não asfaltado: {media_veranistas} ")
print( f"Praias com acesso asfaltado e com menos de 1000 veranistas: {praias_acesso_asfaltado_menos_1000_veranistas}")


    
    
    
    

    
    
    


