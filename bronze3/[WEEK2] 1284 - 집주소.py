while True:
    sum = 2
    n = int(input())

    while n>=10:

        if n%10==1:
            sum=sum+2
        elif n%10==0:
            sum=sum+4
        else:
            sum=sum+3
        n=n//10
        sum = sum + 1


    if n % 10 == 1:
        sum = sum + 2
    elif n % 10 == 0:
        sum = sum + 4
    else:
        sum = sum + 3

    if n==0:
        break
    print(sum)

# 1이면 2cm
# 0이면 4cm
# 나머지는 3cm