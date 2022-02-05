"""
#B
n = int(input())
mountain = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    mountain.append([b, a])
mountain.sort()
print(mountain[::-1][1][1])
"""
s = input()
ans = 0
for i in range(10000):
    ok = True
    x = "%04d" % (i)
    for j in range(10):
        if s[j] == "o":
            if str(j) not in x:
                ok = False
        if s[j] == "x":
            if str(j) in x:
                ok = False
        if s[j] == "?":
            continue
        print(x)
    if ok:
        ans += 1
print(ans)