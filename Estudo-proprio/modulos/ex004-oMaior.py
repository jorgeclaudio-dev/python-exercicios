A = float(input("Primeiro número: "))
B = float(input("Segundo número: "))
C = float(input("Terceiro número: "))

if A == B == C:
    print("Todos são iguais")
elif A >= B and A >= C:
    print(f"O número {A} é maior que {B} e {C}")
    
elif B >= A and B >= C:
    print(f"O número {B} é maior que {A} e {C}")
else:
    print(f"O número {C} é maior que {A} e {B}")