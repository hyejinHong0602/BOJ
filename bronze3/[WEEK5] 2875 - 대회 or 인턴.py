n, m, k = map(int,input().split())
res=0
while n+m>=k and n>=0 and m>=0:
    n-=2
    m-=1
    res+=1
print(res-1)