continua = True
lista_respostas_aluno = []
qtdAlunosMenosDezVezes = 0
qtdAlunosDezQuinzeVezes = 0
qtdAlunosMaisQuinzeVezes = 0
        
while continua: 
    
    numero_vezes = int(input("Quantas vezes você utilizou o restaurante? Resposta: "))    
    lista_respostas_aluno.append(numero_vezes)    
    
    teste_nova_pergunta = input("\nDeseja perguntar para outro aluno [S]im ou [N]ão: ")
    if teste_nova_pergunta.upper().startswith('N'):
        continua = False


for resposta in lista_respostas_aluno:
    if resposta < 10:
        qtdAlunosMenosDezVezes = qtdAlunosMenosDezVezes + 1 
    elif resposta <= 15:
        qtdAlunosDezQuinzeVezes = qtdAlunosDezQuinzeVezes + 1
    else:
        qtdAlunosMaisQuinzeVezes = qtdAlunosMaisQuinzeVezes + 1

qtdRespostas = len(lista_respostas_aluno)
percAlunosMenosDezVezes = qtdAlunosMenosDezVezes / qtdRespostas * 100.0
percAlunosDezQuinzeVezes = qtdAlunosDezQuinzeVezes / qtdRespostas * 100.0
percAlunosMaisQuinzeVezes = qtdAlunosMaisQuinzeVezes / qtdRespostas * 100.0

print("")
print( f"Entrevista com {qtdRespostas} aluno(s) sobre a frequência no restaurante" )
print( '-' * 80 )
print( f"{percAlunosMenosDezVezes:.2f}% frequentaram até 10 vezes" )
print( f"{percAlunosDezQuinzeVezes:.2f}% frequentaram entre 10 e 15 vezes" )
print( f"{percAlunosMaisQuinzeVezes:.2f}% frequentaram mais de 15 vezes" )

