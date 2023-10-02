string = input("Введите строку символов: ")
compressed = ""
count = 1

for i in range(0, len(string) - 1):
    if string[i] == string[i + 1]:
        count += 1
    else:
        if count > 1:
            compressed += string[i] + str(count)
        else:
            compressed += string[i]
        count = 1
# отдельный вывод последнего символа, т.к. после него нет отличных символов
if count > 1:
    compressed += string[-1] + str(count)
else:
    compressed += string[-1]

print(compressed)
