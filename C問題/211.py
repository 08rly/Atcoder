"""
#B
l = ["H" , "2B" , "3B" , "HR"]
s = []
for _ in range(4):
    s.append(input())
l.sort()
s.sort()
print("Yes" if l == s else "No")
"""
t = " chokudai"
mod = 10**9 + 7
dp = [0] * 9
dp[0] = 1

s = input()
for i in s:
    for j in range(9):
        if t[j] == i:
            dp[j] += dp[j-1]
            dp[j] %= mod
        print(dp)
print(dp[-1])