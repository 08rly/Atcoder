"""
#B
import math
a, b, w = map(int, input().split())
w = w*10**3
upper = int(math.floor(w/a))
lower = int(math.ceil(w/b))
if lower > upper:
    print("UNSATISFIABLE")
else:
    print(lower, upper)
"""
n = int(input())
ans = 0
if n >= 10**3: 
    ans += n-999
if n >= 10**6:
    ans += n-999999
if n >= 10**9:
    ans += n-999999999
if n >= 10**12:
    ans += n-999999999999
if n >= 10**15:
    ans += n-999999999999999
print(ans)