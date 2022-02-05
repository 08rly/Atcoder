"""
#B
a, b, c, d = map(int, input().split())
blue = a
red = 0
ans = 0
if b >= c*d:
    print(-1)
    exit()
while True:
    blue += b
    red += c
    if blue <= red*d:
        ans += 1
        break
    else:
        ans += 1
print(ans)
"""

n = int(input())
a = []
for i in range(n):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    a.append([l, r])
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if max(a[i][0], a[j][0]) <= min(a[i][1], a[j][1]):
            ans += 1
print(ans)