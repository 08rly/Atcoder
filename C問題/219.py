"""
#B問題
s1, s2, s3 = input(), input(), input()
S = [s1, s2, s3]
t = list(input())
t = [int(_) for _ in t]
l = []
for i in t:
    l.append(S[i-1])
print("".join(l))
"""
f = lambda:input()
x = list(f())
n = int(f())
s = []
az = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    S = input()
    t = ""
    for j in S:
        p = x.index(j)
        t += az[p]
    s.append((t, S))
s.sort()
for i in range(n):
    print(s[i][1])