a=int(input())
b=int(input())
c=int(input())

res=a*b*c
n=1#자릿수
numbers=[0,0,0,0,0,0,0,0,0,0]
while res>10:
    res=res//10
    n=n+1

res=a*b*c
for i in range(n):
    t=res % 10
    res = res // 10
    for j in range(10):
        if t==j:
            numbers[j]=numbers[j]+1

for k in range(10):
    print(numbers[k])