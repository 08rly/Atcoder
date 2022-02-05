n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

cri = b[0][0]
for i in range(n):
    for j in range(m):
        #AとBが同じか判定
        if b[i][j] != cri+i*7+j:
            print("No")
            exit()
#
cri_ij = (cri%7-1)%7
print("Yes" if m<= 7-cri_ij else "No")