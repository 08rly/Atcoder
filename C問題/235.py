"""
#B
n = int(input())
h = list(map(int, input().split()))
ans = h[0]
for i in range(1, n):
    if h[i-1] < h[i]:
        ans = h[i]
    else:
        break
    if h[i] == h[n-1] or h[i-1] == h[i]:
        break
print(ans)
"""
from collections import defaultdict
n, q = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(list)
for i, x in enumerate(a, 1):
    d[x].append(i)

for i in range(q):
    x, k = map(int, (input().split()))
    if k <= len(d[x]):
        print(d[x][k-1])
    else:
        print(-1)