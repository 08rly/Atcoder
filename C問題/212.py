"""
#B
x = input()
if x[0] == x[1] == x[2] == x[3]:
    print("Weak")
    exit()
for i in range(3):
        if (int(x[i+1]))%10 != (int(x[i])+1)%10:
            print("Strong")
            exit()
print("Weak")
"""
from bisect import bisect_left as bl

INF = 10**10

n, m = map(int, input().split())
a = list(map(int ,input().split()))
b = list(map(int ,input().split())) + [-INF, INF]
a.sort()
b.sort()
ans = 10**9+1
for i in a:
    index = bl(b, i)
    ans = min(ans, abs(i - b[index]),abs(i- b[index-1]))
print(ans)
