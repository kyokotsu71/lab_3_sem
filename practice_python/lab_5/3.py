sett = set()
n = int(input("Введите количество названных городов: "))
for _ in range(n):
    sett.add(input())
new = input("Введите новый город: ")
if new in sett:
    print("REPEAT")
else:
    print("OK")
    sett.add(new)
