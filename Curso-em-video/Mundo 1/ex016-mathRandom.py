import random

alunoA = str(input("Nome do 1º aluno: "))
alunoB = str(input("Nome do 2º aluno: "))
alunoC = str(input("Nome do 3º aluno: "))
alunoD = str(input("Nome do 4º aluno: "))
nomes = [alunoA, alunoB, alunoC, alunoD]
print(f"O aluno(a) que apagará o quadro é: {random.choice(nomes)}")