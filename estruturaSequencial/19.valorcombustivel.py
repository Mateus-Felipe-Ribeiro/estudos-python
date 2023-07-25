kmPorLitro = 20
custoLitro = 5

dinheiro = float(input("Quanto de dinheiro possuí? R$"))

quantidadeCombustivel = dinheiro/custoLitro
kmsPossiveis = quantidadeCombustivel * kmPorLitro

print("A quantidade de combustível possível de comprar é:",quantidadeCombustivel,"l")
print("A quantidade de KM que o veículo poderá rodar é:",kmsPossiveis,"km")