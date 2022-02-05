"""
#B
s = input()
ans = ''
for i in s:
    if i == "6":
        ans += "9"
    elif i == "9":
        ans += "6"
    else:
        ans += i
print(ans[::-1])
"""
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ca = Counter(a)
ans = 0
for i in c:
    j = i-1
    k = b[j]
    ans += ca[k]
print(ans)