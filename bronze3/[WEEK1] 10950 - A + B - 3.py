t=int(input())
sum=[]
for i in range(t):
    a,b=map(int,input().split())
    sum.append(a+b)

for j in range(t):
    print(sum[j])
