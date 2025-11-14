from math import ceil, floor

# dados do aluno
nome = str(input("Qual o nome do aluno(a): "))
ativ = float(input("Qual foi a nota da atividade: "))
prova = float(input("Qual foi a nota da prova: "))
trabalho = float(input("Qual foi a nota do trabalho: "))
fator = int(input("Aluno(a) comportado(a): \n[1] Sim\n[2] Não\n"))

# condições
if all(0 <= n <= 10 for n in [ativ, prova, trabalho]) and fator in [1, 2]:
    print("Qual o peso das notas: ")
else:
    print("Erro, notas inválidas ou fator inexistente")
    exit()

# pesos das notas para cálculo da média
peso_atv = float(input("Atividade: "))
peso_prova = float(input("Prova: "))
peso_trab = float(input("Trabalho: "))
#formula
peso = peso_atv + peso_prova + peso_trab
media = (ativ * peso_atv + prova * peso_prova + trabalho * peso_trab) / peso

if fator == 1:
    media = ceil(media)
elif fator == 2:
    media = floor(media)

if media >= 6.5:
    print(f"O aluno(a): {nome}\nFoi aprovado com média {media}!")
else:
    print(f"O aluno(a): {nome}\nEstá em recuperação com média {media}! (estude mais!!)")