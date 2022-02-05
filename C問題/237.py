"""
#B
h, w = map(int, input().split())
a = [list(input().split()) for _ in range(h)]
l = []
for i in range(w):
    l2 = []
    for j in range(h):
        s = a[j][i]
        l2.append(s)
    l.append(l2)
for i in l:
    print(*i)
"""
"""
#D
n = input()
s = input()
L, R = [], []
for i, c in enumerate(s):
    if c == 'L':
        R.append(i)
    else:
        L.append(i)
print(*(L+[n]+R[::-1]))
"""
s = input()
cnt = 0
for i in s[::-1]:
    if i != "a":
        break
    cnt += 1
for i in s:
    if i != "a":
        break
    cnt -= 1
ans = "a"*cnt+s
if ans == ''.join(reversed(ans)):
    print("Yes")
else:
    print("No")