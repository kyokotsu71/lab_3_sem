set1 = set(input("1-е множество: ").split())
set2 = set(input("2-е множество: ").split())

if set1 == set2:
    print(False)
    exit(0)

if set1.issubset(set2):
    print(True)
elif set2.issubset(set1):
    print(True)
else:
    print(False)
