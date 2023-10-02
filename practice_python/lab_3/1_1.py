string = input("Введите строку символов: ")
decompressed = ""
count = 1

for i in range(0, len(string)-1):
    if string[i + 1].isdigit():
        decompressed += string[i] * int(string[i + 1])
    elif not string[i].isdigit():
        decompressed += string[i]

if not string[-1].isdigit():
    decompressed += string[-1]
print(decompressed)