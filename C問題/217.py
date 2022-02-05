"""
#B問題
s1, s2, s3 = input(), input(), input()
S = [s1, s2, s3]
l = ['ABC', 'ARC', 'AGC', 'AHC']
for i in S:
    l.remove(i)
print(l[0])
"""
n = int(input())
p = [0] + list(map(int, input().split()))
q = [0]*(n+1)
for i in range(n+1):
    q[p[i]] = i
print(" ".join(map(str, q[1:])))