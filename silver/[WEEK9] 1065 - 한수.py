n = int(input())
checknum=0
if n <= 99:
    print(n)
else:
    for i in range(100, n+1):
        a = list(str(i))
        for j in range(1, len(a)-1):

            if int(a[j])*2 !=int(a[j-1])+int(a[j+1]):
                break
            else:
                checknum+=1


    print(99+checknum)




