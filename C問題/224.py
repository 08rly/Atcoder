n = int(input())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append((x, y))
    
cnt = 0
for i in range(n):
    x1, y1 = l[i]
    for j in range(i):
        x2, y2 = l[j]
        for k in range(j):
            x3, y3 = l[k]
            if (y3-y1)*(x2-x1) != (y2-y1)*(x3-x1):
                cnt += 1
print(cnt)