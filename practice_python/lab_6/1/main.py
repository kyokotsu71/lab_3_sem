f = open('input.txt', 'r')
numbers = list(map(int, f.read().split()))
f.close()

product = 1
for num in numbers:
    product *= num

f = open('output.txt', 'w')
f.write(str(product))
f.close()
