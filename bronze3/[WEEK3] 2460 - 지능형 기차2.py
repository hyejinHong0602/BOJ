M=0
sum=0
for i in range(10):
    a, b=map(int, input().split())
    sum-=a
    sum+=b
    if sum>M:
        M=sum
print(M)