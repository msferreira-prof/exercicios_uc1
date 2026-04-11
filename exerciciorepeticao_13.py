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
    
# programa principal
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

# for candidato in candidatos:
#     print(candidato)

## calcular a media dos candidatos e verificar se foi aprovado
soma_nota_prova_portugues = 0.0
numero_candidatos_media_conhecimentos_gerais = 0
numero_candidatos_aprovado_matematica = 0
lista_nomes_aprovados = []

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
        lista_nomes_aprovados.append(candidato.nome)
        
    # definir a media da prova de Portugues
    soma_nota_prova_portugues = soma_nota_prova_portugues + candidato.nota_portugues

    # definir media > 4.5 e nota de Conhecimentos Gerais > 6.0
    if candidato.media > 4.5 and candidato.nota_conhecimentos_gerais > 6.0: 
        numero_candidatos_media_conhecimentos_gerais += 1

    # definir numero candidatos aprovados nota em Matemática acima de 5
    if candidato.situacao == "Aprovado" and candidato.nota_matematica > 5.0: 
        numero_candidatos_aprovado_matematica += 1
 

# calcular media da prova de portugues
media_prova_portugues = soma_nota_prova_portugues / len(candidatos)

# saida
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
print( f"Candidatos com média maior que 4.5 e nota de Conhecimentos Geral maior que 6,0 {numero_candidatos_media_conhecimentos_gerais}" ) 

print()
print("-" * 80)
print( f"Candidatos aprovados com nota de Matematica maior que 5,0: {numero_candidatos_aprovado_matematica}" ) 

