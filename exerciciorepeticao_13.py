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

for candidato in candidatos:
    print(candidato)