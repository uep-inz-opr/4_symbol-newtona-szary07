import math

wejscie = map(int, input().split())
x = list(wejscie)

x1 = x[0]
x2 = x[1]
tablica_wynikow1 = []
tablica_wynikow2 = []

while x1 >= 1:
    tablica_wynikow1.append(x1)
    x1 = x1 - 1

while x2 >= 1:
    tablica_wynikow2.append(x1)
    x2 = x2 - 1

print(tablica_wynikow1)
print(tablica_wynikow2)

mnozenie1 = math.prod(tablica_wynikow1)
mnozenie2 = math.prod(tablica_wynikow2)
print(mnozenie1, mnozenie2)