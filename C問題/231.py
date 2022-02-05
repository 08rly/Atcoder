import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
x = []
for i in range(q):
    x.append(int(input()))

print(a)
print(x)
for j in x:
    num = bisect.bisect_left(a, j)
    print(num)
    print(len(a)-num)