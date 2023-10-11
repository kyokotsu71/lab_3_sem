ls = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
words = dict()

for x in ls:
    words[x] = 0
for i in range(len(ls)):
    words[ls[i]] += 1

print(*list(words.values()))
