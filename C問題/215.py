"""
#B問題
n = int(input())
flag = True
k = 0
while flag:
    if 2**k <= n:
        k += 1
    else:
        flag = False
print(k-1)
"""
import itertools as it
sk = list(input().split())
k = int(sk[-1])
del sk[-1]
ans = set()
s = list("".join(sk))
for word in it.permutations(s):
    ans.add("".join(word))
print(sorted(ans)[k-1])