n = int(input())
ans = 100000000000000000000
for i in range(n):
    a, p, x = map(int, input().split())
    if x > a:
        ans = min(ans, p)
        
print(ans if ans != 100000000000000000000 else -1)
