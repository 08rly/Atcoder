"""
#B
n, k = map(int, input().split())
ans = 0
for i in range(1,n+1):
    for j in range(1, k+1):
        ans += i*100 + j
print(ans)
"""
n, k = map(int, input().split())
l = []
for i in range(n):
    ab = list(map(int, input().split()))
    l.append(ab)
l.sort()
now_village = k

for i in range(n):
    friend_place = l[i][0]
    friend_money = l[i][1]
    
    if now_village >= friend_place:
        now_village += friend_money
    else:
        break
print(now_village)