num = int(input("Digite um número inteiro: "))
n = 1

if num >= 0:
    while n < 11:
        mult = num * n
        print(f"{num:3} x {n:2} = {mult:3}")
        n = n + 1
    
    print("Fim da tabuada!")
else:
    print("Digite um número positivo!")