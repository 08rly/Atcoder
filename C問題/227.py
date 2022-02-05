n = int(input())
ans = 0
for a in range(1, n+1):
    if a**3 > n:
        break
    for b in range(1, n+1):
        if a*b*b > n:
            break
        ab = a*b
        min_c = b
        max_c = n // ab
        ans = max_c - min_c  + 1
print(ans)