from math import cos, sin, tan, radians

num = float(input("Informe o ângulo: °"))
angulo_rad = radians(num)
print(f"Cosseno {cos(angulo_rad):.3f}\nSeno {sin(angulo_rad):.3f}\nTangente {tan(angulo_rad):.3f}")