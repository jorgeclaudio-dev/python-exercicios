num = int(input('Digite o número secreto: '))
contador = 0
soma = 0
while num != 0:
    soma += num
    num = int(input('Digite o número secreto: '))
    contador += 1
print(f"Você digitou {contador} números")
print(f"A soma total: {soma}")