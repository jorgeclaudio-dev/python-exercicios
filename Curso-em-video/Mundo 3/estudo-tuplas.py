lanches = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata Frita')

#print(len(lanches))

#for c in lanches:
#    print(c)

# Se for necessário descobrir a posição, usando range
#for cont in range(0, len(lanches)):
#    print(f'Eu vou comer {lanches[cont]} na posição {cont}')

# Se for necessário descobrir a posição, usando pos e enumerate
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi Muito!!')
