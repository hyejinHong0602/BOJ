n=int(input())

for i in range(0,n):
    for j in range(i):
        print(' ',end='')
    for k in range(2*(n-i-1)+1):
        print("*",end='')
    print()

for i in range(1,n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()