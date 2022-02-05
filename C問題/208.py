"""
#B
from math import factorial
p = int(input())
ans = 0
for i in range(11, 0, -1):
    ans += p // factorial(i)
    p %= factorial(i)
print(ans)
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
lst = [(a[i], i) for i in range(n)]
lst.sort()
none = k%n
all = k//n
snack = [all]*n
for i in range(n):
    index = lst[i][1]
    if none >= 1:
        snack[index] += 1
        none -= 1
for i in range(n):
    print(snack[i])