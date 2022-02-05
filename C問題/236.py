n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())
T = set(t)
for i in s:
    print("Yes" if i in T else "No")