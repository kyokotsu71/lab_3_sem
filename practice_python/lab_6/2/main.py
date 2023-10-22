f = open('input.txt', 'r')
numbers = [int(line.strip()) for line in f]
f.close()

numbers = sorted(numbers)

f = open('output.txt', 'w')
for i in numbers:
    f.write(str(i))
    f.write('\n')
f.close()
