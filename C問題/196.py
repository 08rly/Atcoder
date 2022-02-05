"""
#B
x = input().split(".")
print(x[0])
"""
n = int(input())
ans = 0
for i in range(1,10**12):
    if int(str(i)*2)<=n:
        ans+=1
    elif int(str(i)*2)>n:
        break
    else:
        pass
print(ans)