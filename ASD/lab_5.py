# сортировка вставками
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
for i in range(1, len(alist)):
    temp = alist[i]
    j = i - 1
    while j >= 0 and temp < alist[j]:
        alist[j + 1] = alist[j]
        j = j - 1
    alist[j + 1] = temp

print('Sorted list: ', end='')
print(alist)
