n,x =map(int, input().split())

a=list(map(int, input().split())) #다시 체크하기

for j in range(n):
    if a[j]<x:
        print(a[j], end=' ')