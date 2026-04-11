class Candidato:
    
    def __init__(self, nome, nota_portugues, nota_matematica, nota_conhecimentos_gerais):
        self.nome = nome
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica
        self.nota_conhecimentos_gerais =  nota_conhecimentos_gerais
        self.media = 0.0
        self.situacao = "Reprovado"

    def __str__(self):
        return f"{nome}"

# entrada 
# receber as informacoes dos candidatos e 
# devolver uma lista com eles
def receber_candidatos():
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

## definir a media e a situacao de candidato na lista
def definir_situacao_candidato(candidatos):

    for candidato in candidatos:
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
     
## calcular media prova portuges    
def calcular_media_prova_portugues(candidatos):
    soma_nota_prova_portugues = 0.0
    for candidato in candidatos:
        # definir a media da prova de Portugues
        soma_nota_prova_portugues = soma_nota_prova_portugues + candidato.nota_portugues

    media_prova_portugues = soma_nota_prova_portugues / len(candidatos)
    
    return media_prova_portugues

## calcular o numero de candidatos com media > 4.5 e nota de conhecimentos_gerais > 6   
def calcular_numero_candidatos_media_conhecimentos_gerais(candidatos):
    numero_candidatos = 0
    for candidato in candidatos:    
        # definir media > 4.5 e nota de Conhecimentos Gerais > 6.0
        if candidato.media > 4.5 and candidato.nota_conhecimentos_gerais > 6.0: 
            numero_candidatos = numero_candidatos + 1
    
    return numero_candidatos
            
##
def calcular_numero_aprovados_matematica(candidatos):
    numero_candidatos_aprovado_matematica = 0
    for candidato in candidatos: 
        # definir numero candidatos aprovados nota em Matemática acima de 5
        if candidato.situacao == "Aprovado" and candidato.nota_matematica > 5.0: 
            numero_candidatos_aprovado_matematica += 1
        
    return numero_candidatos_aprovado_matematica

def listar_aprovados(candidatos):
    lista_nomes_aprovados = []
    for candidato in candidatos:
        if candidato.situacao == "Aprovado":
            lista_nomes_aprovados.append(candidato.nome)
    
    return lista_nomes_aprovados

# saida
def imprimir_resultados(lista_nomes_aprovados, media_prova_portugues, numero_candidatos_media_conhecimentos_gerais, numero_candidatos_aprovado_matematica):

    print()
    print("Candidatos aprovados")
    print("-" * 80)
    for nome_candidato in lista_nomes_aprovados:
        print( f"{nome_candidato}")    

    print()
    print("-" * 80)
    print( f"A média da prova de Portugues foi {media_prova_portugues:.2f}")

    print()
    print("-" * 80)
    print( f"Candidatos com média maior que 4.5 e nota de Conhecimentos Geral maior que 6,0: {numero_candidatos_media_conhecimentos_gerais}" ) 

    print()
    print("-" * 80)
    print( f"Candidatos aprovados com nota de Matematica maior que 5,0: {numero_candidatos_aprovado_matematica}" ) 
    

    
# programa principal
candidatos = receber_candidatos()

# processamento
definir_situacao_candidato(candidatos)
media_prova_portugues = calcular_media_prova_portugues(candidatos)
numero_candidatos_media_conhecimentos_gerais = calcular_numero_candidatos_media_conhecimentos_gerais(candidatos)
numero_candidatos_aprovado_matematica = calcular_numero_aprovados_matematica(candidatos)
lista_nomes_aprovados = listar_aprovados(candidatos)

# saida
imprimir_resultados(lista_nomes_aprovados, media_prova_portugues, numero_candidatos_media_conhecimentos_gerais, numero_candidatos_aprovado_matematica)

