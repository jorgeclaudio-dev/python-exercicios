valor = float(input("Qual é o salário do funcionário: R$"))
aumento = valor + (valor * 15 / 100)
print(f"Um funcionário que ganhava R${valor:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}")