n = int(input("Введите глубину треугольника: "))
n = (3 ** n)
triangle = []
for i in range(n):
    row = []
    for j in range(i+1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
    triangle.append(row)


for row in triangle:
    for i in range(len(row)):
        if row[i] % 3 == 1 or row[i] % 3 == 2:
            row[i] = '*'
        else:
            row[i] = ' '
    print(' '*n, *row, sep=' ')
    n -= 1
