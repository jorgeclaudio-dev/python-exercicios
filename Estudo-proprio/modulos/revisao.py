def soma(a, b):
    return a + b

a1, b1 = (input("Digite dois valores separados por espaço: ")).split()
a1 = int(a1)
b1 = int(b1)
print(f"{a1} + {b1} = {soma(a1, b1)}")