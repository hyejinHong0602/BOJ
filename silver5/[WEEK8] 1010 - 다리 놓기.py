t = int(input())


for i in range(t):
    res = 1
    n, m = map(int,input().split())
    for j in range(m, m-n, -1):
        res*=j
    for k in range(n,0, -1):
        res//=k
    print(res)