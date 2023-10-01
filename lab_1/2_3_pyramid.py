# не работает
n = int(input("Enter N: "))
if n > 9:
    width = n * 2
else:
    width = n * 2 - 1

for i in range(n+1):
    x = str()
    for j in range(1, i):
        x += str(j)
    for j in range(i, 0, -1):
        x += str(j)
    print(x.center(width))
    if i > 8:
        print()
        if i > 98:
            print()
print(width)