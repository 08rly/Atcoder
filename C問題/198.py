"""
#B
n = input()
N = n.rstrip('0')
if N == N[::-1]:
    print('Yes')
else:
    print('No')
"""
from math import sqrt
from math import ceil
r, x, y = map(int, input().split())
step = sqrt(x**2+y**2)
if step == r:
    print(1)
elif step <= r*2:
    print(2)
else:
    print(ceil(step/r))