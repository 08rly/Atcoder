"""
#B
n = int(input())
a = list(map(int, input().split()))
A = a.copy()
A.sort()
s =A.pop(-2)
print(a.index(s)+1)
"""
import bisect
h, w, n = map(int, input().split())

A, B, l = [], [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    l.append([a, b])
A = list(set(A))
B = list(set(B))
A.sort()
B.sort()
for i in l:
    a=bisect.bisect_left(A, i[0])+1
    b=bisect.bisect_left(B, i[1])+1
    print(a, b)