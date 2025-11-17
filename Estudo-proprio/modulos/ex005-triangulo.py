A = float(input("Diga um número: "))
B = float(input("Diga outro número: "))
C = float(input("Diga o último número: "))
if (A < B + C) and (B < A + C) and (C < A + B):
    print("Pode formar um triângulo")
else:
    print("Não forma um triângulo")