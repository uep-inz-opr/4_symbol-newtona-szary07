import math

wejscie = map(int, input().split())
x = list(wejscie)

x1 = x[0]
x2 = x[1]
x3 = x1 - x2

tablica_wynikow1 = []
tablica_wynikow2 = []
tablica_wynikow3 = []

while x1 >= 1:
    tablica_wynikow1.append(x1)
    x1 = x1 - 1

while x2 >= 1:
    tablica_wynikow2.append(x2)
    x2 = x2 - 1

while x3 >= 1:
    tablica_wynikow3.append(x3)
    x3 = x3 - 1

#print(tablica_wynikow1)
#print(tablica_wynikow2)
#print(tablica_wynikow3)

n_silnia = math.prod(tablica_wynikow1)
k_silnia = math.prod(tablica_wynikow2)
n_k_silnia = math.prod(tablica_wynikow3)

symbol_newtona = n_silnia/(k_silnia*n_k_silnia)
print(int(symbol_newtona))
