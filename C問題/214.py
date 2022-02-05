"""
#b
s, t = map(int, input().split())
ans = 0
for a in range(s+1):
    for b in range(s+1-a):
        for c in range(s+1-a-b):
            if a*b*c <= t:
                ans += 1
            
print(ans)
"""
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split())) 
for i in range(n*2):
    t[(i+1)%n] = min(t[(i+1)%n], t[i%n]+s[i%n])

for ans in t:
    print(ans)