"""
#B
n = int(input())
total = 0
i, ans = 1, 0
while total < n:
    total += i
    ans += 1
    i += 1
print(ans)
"""
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dd = defaultdict(int)
for i in a:
    if i not in dd:
        dd[i] = 0
    dd[i] += 1
ans = 0
for i in range(n):
    dd[a[i]] -= 1
    ans += (n-1-i)-dd[a[i]]
print(ans)