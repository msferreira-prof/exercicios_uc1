## programa principal
import exerciciorepeticao_13_v4_modulo as v4m

# entrada
candidatos = v4m.informar_candidatos()

# processamento
# calcular media e avaliar aprovacao
v4m.calcular_media_candidatos(candidatos)

# calcular media prova portugues
media_prova_portugues = v4m.calcula_media_portugues(candidatos)

# calcular numero candidados media conhec gerais
numero_candidatos_media_conhecimentos_gerais = v4m.calcular_numero_candidatos_conhec_gerais(candidatos)

# calcular numero aprovados matematica > 5.0
numero_candidatos_aprovado_matematica = v4m.calcular_aprovados_matematica(candidatos)

# recuperar lista nomes aprovados
lista_nomes_aprovados = v4m.recuperar_lista_aprovados(candidatos)

# saida
# apresentar resultados
v4m.apresentar_resultados(media_prova_portugues, numero_candidatos_media_conhecimentos_gerais
                         , numero_candidatos_aprovado_matematica, lista_nomes_aprovados)    
  