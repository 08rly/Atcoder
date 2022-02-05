"""
B問題
k = int(input())
a, b = input().split()
A = int(a, k)
B = int(b, k)
print(A*B)
"""
#-------------------------------------#
n = int(input())
a = list(map(int, input().split()))
x = int(input())
s = sum(a)

period = x//s 
ans = period*len(a)
sum = period*s
for i in range(len(a)):
    sum += a[i]
    ans += 1
    if sum > x:
        break
print(ans)