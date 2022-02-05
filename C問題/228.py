n, k = map(int, input().split())
li = []
for i in range(n):
    p = map(int,input().split())
    li.append(sum(p))

P = li.copy()
li.sort(reverse=True)
for j in P:
    if j + 300 >= li[k-1]: #300点足して上位ｋ位以上に入れるか
        print("Yes")
    else:
        print("No")