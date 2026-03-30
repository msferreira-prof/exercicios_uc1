salario_bruto = float(input("Informe o salário: "))
desconto = salario_bruto * 0.2
salario_liquido = salario_bruto - desconto
print(f"O salário líquido: {salario_liquido:.2f}")
print("O salario liquido: " + str(salario_liquido))
print("O salário líquido: {0:.2f}".format(salario_liquido))
