idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 120:
    print("Idade inválida, tente novamente.")
    idade = int(input("Digite sua idade: "))
print("Idade registrada com sucesso!")