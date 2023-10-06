s = input("Введите строку: ")
t = ([(s.count(i), i) for i in s if i != ' '])
print(sorted(set(t))[::-1][:3])
