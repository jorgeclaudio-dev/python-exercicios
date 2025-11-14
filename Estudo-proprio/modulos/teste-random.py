import random

# exemplo de rpg de mesa D&D
print("Um dragão apareceu, você ataca ele! jogue seu dado: ")
print("=" * 15, "\n[1] para D20\n[2] para D12\n[3] para D10\n[4] para D08\n[5] para D06\n[6] para D04\n", "=" * 15)
opcao = int(input("Qual dado você usa: "))

lados = {
    1: 20,
    2: 12,
    3: 10,
    4: 8,
    5: 6,
    6: 4
}

if opcao in lados:
    dado = lados[opcao]
    sorte = random.randint(1, dado)
    print(f"Você rolou um D{dado} e tirou {sorte}")
    
else:
    print("Erro, opção inválida")