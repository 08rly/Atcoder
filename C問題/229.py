n, w = map(int, input().split())
li = []
for i in range(n):
    a, b = map(int, input().split())
    li.append([a, b])

li.sort(reverse=True)
ans = 0
for i in range(n):
    point = li[i][0]
    weight = li[i][1]
    if weight <= w:
        ans += point * weight
        w -= weight
    else:
        ans += point * w
        break

print(ans)