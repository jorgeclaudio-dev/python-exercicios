num = int(input("Digite o número secreto: "))
par = 0
impar = 0
while num != 0:

    if num % 2 == 0:
        par += 1

    else:
        impar += 1
        
    num = int(input("Digite o número secreto: "))

print(f"Números errados até acertar:")
print(f"Pares: {par}")
print(f"Ímpares: {impar}")