numero = int(input("Informe um número inteiro: "))

if numero > 0:
    resultado = "positivo"
elif numero < 0:
    resultado = "negativo"
else:
    resultado = "zero"

mensagem = f"O meu número {numero} é {resultado}"
print(mensagem)
