from itertools import product

#main
n, m = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
choice = [tuple(map(int, input().split())) for _ in range(k)]

ans = 0
for pro in product(*choice):
    sum = 0
    cnt = 0
    for a, b in conditions:
        if a in pro and b in pro:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)