n = int(input())
A = []
B = []
time = 0
length = 0
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    time += a/b

time = time/2

for a, b in zip(A, B):
    if time <= a/b:
        length += time*b
        break
    else:
        length += a
        time -= a/b
    
print(length)