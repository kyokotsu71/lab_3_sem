# Поразрядная сортировка

arr = [170, -45, -75, 90, -802, 24, 2, 66, 123]
digits = len(str(max(arr)))

buckets = [[] for _ in range(len(arr)+1)]

for d in range(digits):
    for num in arr:
        digit = (num // 10 ** d) % 10
        buckets[digit].append(num)

    arr = [num for bucket in buckets for num in bucket]

    buckets = [[] for _ in range(10)]

negatives = [num for num in arr if num < 0]
positives = [num for num in arr if num >= 0]
arr = negatives + positives

print(arr)

