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