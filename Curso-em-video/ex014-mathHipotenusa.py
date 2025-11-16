from math import acos, asin, atan, pow,sqrt

cat_opos = float(input("Qual o comprimento do cateto oposto: "))
cat_adj = float(input("Qual o comprimento do cateto adjacente: "))
hipo = sqrt(pow(cat_opos, 2) + pow(cat_adj, 2))

print(f"A hipotenusa é {hipo}")