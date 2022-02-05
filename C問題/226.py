import sys
sys.setrecursionlimit(10000000)
n = int(input())
t, k, a =[], [], []
for i in range(n):
    s = list(map(int, input().split()))
    t.append(s[0])
    k.append(s[1])
    a.append(s[2:])
ans = 0

tf = [False]*n

def graph(i):
    i -= 1
    if not tf[i]:
        tf[i] = True
        global ans
        ans += t[i]
        if len(a[i]) != 0:
            for j in a[i]:
                graph(j)

tf[n-1] = True
for i in a[n-1]:
    graph(i)

print(ans+t[n-1])