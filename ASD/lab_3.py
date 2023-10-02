# На вход дается одно число х, нужно вывести все числа от 1 до х, удовлетворяющие условию:
# 3^K * 5^L * 7^M = x
# где K, L, M - натуральные числа или могут быть равны 0.
from math import log

x = int(input())
quant = []
for K in range(int(log(x, 3)+1)):
    for L in range(int(log(x, 5)+1)):
        for M in range(int(log(x, 7)+1)):
            n = 3**K * 5**L * 7**M
            if n > x:
                break
            quant.append(n)


print(quant)
