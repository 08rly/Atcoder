"""
#B問題
n = int(input())
name_list = set()
for i in range(n):
    s, t = input().split()
    name_list.add(tuple([s, t]))
print("Yes" if n != len(name_list) else "No")
"""
N = int(input())
ans = []
for i in range(N):
    if N == 1:
        ans.append("A")
        break
    if N % 2 == 1:
        N -= 1
        ans.append("A")
    else:
        N //= 2
        ans.append("B")
print("".join(ans[::-1]))