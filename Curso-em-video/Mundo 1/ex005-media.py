nome = str(input('Nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
trabalho = float(input('Nota do trabalho: '))
media = (nota1 + nota2 + trabalho) / 3

print(f'O aluno(a) {nome}, teve a média de {media:.1f}.')

if media >= 6:
    print(f'O aluno(a) {nome} foi APROVADO!')
else:
    print(f'O aluno(a) {nome} está em RECUPERAÇÃO!')