"""
#B
n, x = map(int, input().split())
a = list(map(int, input().split()))
tmp = 0
for i in range(n):
    if i % 2 == 0:
        tmp += a[i]
    else:
        tmp += a[i]-1
print("Yes" if x>=tmp else "No")
"""
n = int(input())
c = list(map(int, input().split()))
c.sort()
MOD = 10**9+7
ans = 1
for i in range(n):
    ans *= max(0, c[i]-i)
    ans %= MOD
print(ans)