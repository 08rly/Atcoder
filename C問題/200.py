"""
#B
n, k = map(int, input().split())
for i in range(k):
    if n % 200 == 0:
        n = n // 200
    else:
        n = int(str(n)+ "200")
print(n)
"""
n = int(input())
a = map(int, input().split())
cnt = [0]*200
for x in a:
    cnt[x%200] += 1
ans = 0
for x in cnt:
    ans += (x*(x-1))//2
print(ans)