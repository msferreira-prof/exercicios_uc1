import minhas_classes as mc

# programa
meuCao = mc.Cao(10, "poodle" )
peso = meuCao.peso
raca = meuCao.raca
print( f"Meu {raca} pesa {peso} Kg")
meuCao.latir()

meu_outro_cao = mc.Cao(12, "labrador")
print( f"Meu outro cão é um {meu_outro_cao.raca} e pesa {meu_outro_cao.peso} Kg")
meu_outro_cao.latir()

print(meuCao)
print(meu_outro_cao)

meu_golden = mc.Golden(15, "creme claro")
peso = meu_golden.peso
raca = meu_golden.raca
cor_pelo = meu_golden.cor_pelo
print( f"Meu {raca} pesa {peso} Kg e tem pelo da cor {cor_pelo}")
meu_golden.latir()
meu_golden.sentar()