"""
#B
n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(1, n+1):
    l.append(i)
a.sort()

print("Yes" if a == l else "No")
"""
a, b, c = map(int, input().split())

if c%2 == 0:
    if abs(a) > abs(b):
        print(">")
    elif abs(a) < abs(b):
        print("<")
    else:
        print("=")
else:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")