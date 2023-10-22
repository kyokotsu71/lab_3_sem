oldest = None
youngest = None

f = open('input.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    surname, name, age = line.strip().split()
    age = int(age)

    if oldest is None or age > oldest[2]:
        oldest = (surname, name, age)

    if youngest is None or age < youngest[2]:
        youngest = (surname, name, age)

with open("oldest.txt", "w", encoding='utf-8') as file:
    file.write(f'{oldest[0]} {oldest[1]} {oldest[2]}')

with open("youngest.txt", "w", encoding='utf-8') as file:
    file.write(f'{youngest[0]} {youngest[1]} {youngest[2]}')
