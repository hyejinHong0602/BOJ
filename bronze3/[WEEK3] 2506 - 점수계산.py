n=int(input()) #문제 수
t=list(map(int,input().split()))
sum=0
res=0
for i in range(n):
    if t[i]==1:
        sum+=1
        res+=sum
    else:
        sum=0
print(res)