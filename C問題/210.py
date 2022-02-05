"""
#B
n = int(input())
s = input()
S = s.index("1")
if int(S)% 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
"""
n, k = map(int, input().split())
c = list(map(int, input().split()))
from collections import Counter
cnt = Counter(c[:k])
tmp = len(set(c[:k]))
ans = tmp
for i in range(n-k):
    cnt[c[i]] -= 1
    if cnt[c[i]] == 0:
        tmp -= 1
    cnt[c[i+k]] += 1
    if cnt[c[i+k]] == 1:
        tmp += 1
    ans = max(ans, tmp)
print(ans)
