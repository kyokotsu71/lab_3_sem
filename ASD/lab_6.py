# сортировка посредством выбора
A = [1, 8, -3, 0, 10000, -1023]
for i in range(len(A) - 1):
    min_index = i
    for k in range(i + 1, len(A)):
        if A[k] < A[min_index]:
            min_index = k
    A[i], A[min_index] = A[min_index], A[i]

print(A)
