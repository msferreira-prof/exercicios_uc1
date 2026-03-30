salario_bruto = float(input("Informe o salário: "))
desconto = salario_bruto * 0.2
salario_liquido = salario_bruto - desconto
print(f"Salário líquido: {salario_liquido:.2f}")
print("Salario liquido: " + str(salario_liquido))
print("Salário líquido: {0:.2f}".format(salario_liquido))
