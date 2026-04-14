class Candidato:
    def __init__(self, nome, nota_portugues, nota_matematica, nota_conhecimentos_gerais):
        self.nome = nome
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica
        self.nota_conhecimentos_gerais =  nota_conhecimentos_gerais
        self.media = 0.0
        self.situacao = "Reprovado"

    def __str__(self):
        return f"{self.nome}"

# funcao para entrada de dados
def informar_candidatos():
    candidatos = []
    
    continua = 0
    while continua == 0:
        nome = input("Informe o nome do candidato: ")
        nota_port = float(input("Informe a nota de Português: "))
        nota_mat = float(input("Informe a nota de Matemática: "))
        nota_conhec = float(input("Informe a nota de Conhecimentos Gerais: "))

        # criar objeto candido e inserir na lista de candidatos
        candidato = Candidato(nome, nota_port, nota_mat, nota_conhec)
        
        candidatos.append(candidato)
        
        # pergunto se deseja continua e cadastrar uma nova praia
        continua = int(input("\nDeseja cadastrar novo candidato (0 - Sim / Qualquer outro número - Não): "))
        print()    

    return candidatos
    
# funcao calcular media e avaliar aprovacao    
def calcular_media_candidatos(lista_candidatos):
    for candidato in lista_candidatos:
        # calcular da media
        media = (candidato.nota_portugues + candidato.nota_matematica + candidato.nota_conhecimentos_gerais) / 3
        candidato.media = media
        
        # verificar se o aluno tem nota abaixo de 2 em qualquer materia
        if candidato.nota_portugues < 2.0 or candidato.nota_matematica < 2.0 or candidato.nota_conhecimentos_gerais < 2.0:
            candidato_tem_nota_abaixo_2 = True
        else:
            candidato_tem_nota_abaixo_2 = False

        # definir a situacao do aluno 
        if candidato.media > 4.0 and candidato_tem_nota_abaixo_2 == False: 
            candidato.situacao = "Aprovado"

# calcular media prova portugues
def calcula_media_portugues(lista_candidatos):
    soma_notas_portugues = 0.0
    for candidato in lista_candidatos:
        soma_notas_portugues = soma_notas_portugues + candidato.nota_portugues
        
    media_portugues = soma_notas_portugues / len(lista_candidatos)        
    return media_portugues

# calcular numero candidados media conhec gerais
def calcular_numero_candidatos_conhec_gerais(lista_candidatos):
    numero_candidatos = 0
    for candidato in lista_candidatos:
        # definir media > 4.5 e nota de Conhecimentos Gerais > 6.0
        if candidato.media > 4.5 and candidato.nota_conhecimentos_gerais > 6.0: 
            numero_candidatos = numero_candidatos + 1
    
    return numero_candidatos

# calcular numero aprovados matematica > 5.0
def calcular_aprovados_matematica(lista_candidatos):
    numero_aprovados = 0
    for candidato in lista_candidatos:
        # definir numero candidatos aprovados nota em Matemática acima de 5
        if candidato.situacao == "Aprovado" and candidato.nota_matematica > 5.0: 
            numero_aprovados += 1
         
    return numero_aprovados

# recuperar lista nomes aprovados
def recuperar_lista_aprovados(lista_candidatos):
    lista_aprovados = []
    for candidato in lista_candidatos:
        if candidato.situacao == "Aprovado":
            lista_aprovados = candidato.nome
    
    return lista_aprovados         
    
# apresentar resultados
def apresentar_resultados( media_portugues, numero_conhec_gerais
                         , numero_aprovados_matematica, lista_nomes_aprovados):
    print()
    print("Candidatos aprovados")
    print("-" * 80)
    for nome_candidato in lista_nomes_aprovados:
        print( f"{nome_candidato}")    

    print()
    print("-" * 80)
    print( f"A média da prova de Portugues foi {media_portugues:.2f}")

    print()
    print("-" * 80)
    print( f"Candidatos com média maior que 4.5 e nota de Conhecimentos Geral maior que 6,0 {numero_conhec_gerais}" ) 

    print()
    print("-" * 80)
    print( f"Candidatos aprovados com nota de Matematica maior que 5,0: {numero_aprovados_matematica}" ) 


## programa principal
# entrada
candidatos = informar_candidatos()

# processamento
# calcular media e avaliar aprovacao
calcular_media_candidatos(candidatos)

# calcular media prova portugues
media_prova_portugues = calcula_media_portugues(candidatos)

# calcular numero candidados media conhec gerais
numero_candidatos_media_conhecimentos_gerais = calcular_numero_candidatos_conhec_gerais(candidatos)

# calcular numero aprovados matematica > 5.0
numero_candidatos_aprovado_matematica = calcular_aprovados_matematica(candidatos)

# recuperar lista nomes aprovados
lista_nomes_aprovados = recuperar_lista_aprovados(candidatos)

# saida
# apresentar resultados
apresentar_resultados(media_prova_portugues, numero_candidatos_media_conhecimentos_gerais
                     , numero_candidatos_aprovado_matematica, lista_nomes_aprovados)    
  