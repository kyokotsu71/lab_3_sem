# хэш таблицы с наложением
with open("input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

table = {}


def hash_function(word):
    value = abs(hash(word)) % 1000
    while str(value) in table:
        value += 1
    return str(value)


for line in lines:
    for word in line.split():
        hash_value = hash_function(word)
        table[hash_value] = word

with open('output.txt', 'w', encoding='utf-8') as file:
    for hash_value, words in table.items():
        file.write(f'{hash_value}: {words}\n')

