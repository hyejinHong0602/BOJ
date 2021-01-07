a,b,c =map(int,input().split())
mid=a
if a>=b:
    if b>=c:
        mid = b
    elif a<=c:
        mid = a
    else:
        mid=c
else:
    if b<=c:
        mid=b
    elif a>=c:
        mid=a
    else:
        mid=c

print(mid)
