# хэш таблицы с наложением
with open("input.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

table = {}


def hash_function(word):
    return str(abs(hash(word)) % 1000)


for line in lines:
    for word in line.split():
        hash_value = hash_function(word)
        if hash_value in table.keys():
            table[hash_value].append(word)
        else:
            table[hash_value] = [word]


with open('output.txt', 'w', encoding='utf-8') as file:
    for hash_value, words in table.items():
        file.write(f'{hash_value}: {words}\n')

