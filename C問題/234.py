"""
#B
import math
n = int(input())
x = [[] for i in range(n)]
y = [[] for i in range(n)]
for i in range(n):
    x[i],y[i] = map(int,input().split())
ans = 0
for j in range(n):
    for t in range(n):
        if math.sqrt(pow(x[t]-x[j],2) + pow(y[t] - y[j],2)) > ans:
            ans = math.sqrt(pow(x[t]-x[j],2) + pow(y[t] - y[j],2))
print(ans)
"""
k = int(input())
k = int(format(k, 'b'))
print(k*2)