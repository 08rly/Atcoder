"""
#B
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] > 10:
        ans += a[i]-10
print(ans)
"""
import sys
sys.setrecursionlimit(10000)
n, m  = map(int, input().split())
graph = [[] for i in range(n)]
#graph[i]は都市iから道路でつながっている都市のリスト
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
def DFS(v):
    if tmp[v]:
        return
    tmp[v] = True
    for to in graph[v]:
        DFS(to)

ans = 0

for i in range(n):
    tmp = [False]*n
    #tmp[j]は都市jに到達可能かどうかを表す
    DFS(i)
    ans += sum(tmp)

print(ans)