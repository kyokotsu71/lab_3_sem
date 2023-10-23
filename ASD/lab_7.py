# Сортировка Шелла

ls = [12, 34, 25, 15, 67, 23, 11, 86]
ls2 = len(ls)//2
while ls2 > 0:
    for i in range(ls2, len(ls)):
        delta = i - ls2
        while delta >= 0 and ls[delta] > ls[i]:
            ls[delta], ls[i] = ls[i], ls[delta]
            i = delta
            delta = i - ls2
    ls2 //= 2

print(ls)
