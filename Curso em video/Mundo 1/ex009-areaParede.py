largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2

print(f"Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.3f}m2.")
print(f"Para pintar essa parede, você presisará de {tinta:.4f}L de tinta")