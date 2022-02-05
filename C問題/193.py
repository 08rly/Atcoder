"""
#B 
n = int(input())
ans = 10**10
for i in range(n):
    A, P, X = map(int, input().split())
    if X - A <= 0:
        pass
    else:
        ans = min(ans, P)
if ans == 10**10:
    print(-1)
else:
    print(ans)
"""
import math
import itertools
n, k = map(int, input().split())
t = [list(map(int, input().split()))for _ in range(n)]
pat = (math.factorial(n-1))
per = [i for i in range(1, n, 1)]
ans = 0
for x in itertools.permutations(per):
    now = 0
    distance = 0

    for y in x:
        distance += t[now][y]
        now = y
    distance += t[now][0]
    if distance == k:
        ans += 1
print(ans)
