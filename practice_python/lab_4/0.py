# Если нужно ввести с клавиатуры
# sps = (input().split())
# sps = [int(x) for x in sps]

ls = [3, 2, -10, 7, 3, 4, 143, 7]
res = []
for i in range(1, len(ls)):
    if ls[i] > ls[i-1]:
        res.append(ls[i])
print(res)
