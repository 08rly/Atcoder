"""
#B
n = int(input())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10**9

for i in range(n):
    for j in range(n):
        if i == j:
            score =A[i]+B[i]
        else:
            score = max(A[i], B[j])
        ans = min(ans, score)
print(ans)
"""
from collections import Counter
n = int(input())
a = [*map(int, input().split())]
cnt = Counter(a)
ans = 0
for x in range(-200, 201):
    for y in range(x+1, 201):
        cx = cnt[x]
        cy = cnt[y]
        ans += cx*cy*(x-y)**2
print(ans)