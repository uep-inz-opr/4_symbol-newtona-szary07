import math

wejscie = map(int, input().split())
x = list(wejscie)

x1 = x[0]
x2 = x[1]
tablica_wynikow = []
while x1 >= 1:
    tablica_wynikow.append(x1)
    x1 = x1 - 1

print(tablica_wynikow)

mnozenie = math.prod(tablica_wynikow)

print(mnozenie)