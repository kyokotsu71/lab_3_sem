n = int(input("Введите кол-во ступенек: "))
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(j + 1, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()
