list1 = [1, 2, 3, 1000, 94, 3, 192334]
list2 = [7, 3, 10, 2, -3, 94, 1, 4531]
list1s = list(set(list1))
same = 0
for i in range(len(list1s)):
    for j in range(len(list2)):
        if list1s[i] == list2[j]:
            same += 1

print(f"В списке {same} совпадающих элементов")
