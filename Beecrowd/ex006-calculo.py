itemA, nitemA, valorA = input("").split()
itemA = int(itemA)
nitemA = int(nitemA)
valorA = float(valorA)

itemB, nitemB, valorB = input("").split()
itemB = int(itemB)
nitemB = int(nitemB)
valorB = float(valorB)

preco = valorA * nitemA + valorB * nitemB

print(f"VALOR A PAGAR: R$ {preco:.2f}")