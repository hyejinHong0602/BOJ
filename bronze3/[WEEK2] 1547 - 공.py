m=int(input())
c=[0,1,0,0]
for i in range(m):
    x, y=map(int,input().split())
    c[x],c[y]=c[y],c[x]
print(c.index(1))