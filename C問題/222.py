n, m = map(int, input().split())
a = [list(input()) for _ in range(2*n)]
rank = [[0, i] for i in range(2*n)]
def janken(a, b):
    if a == b:return -1
    if a == 'G' and b == 'P':return 1
    if a == 'P' and b == 'C':return 1
    if a == 'C' and b == 'G':return 1
    else:return 0

for j in range(m):
    for i in range(n):
        p1 = rank[2*i][1]
        p2 = rank[2*i+1][1]
        result = janken(a[p1][j], a[p2][j])
        if result != -1:
            rank[2*i+result][0] -= 1
    rank.sort()
for i, j in rank:
    print(j+1)