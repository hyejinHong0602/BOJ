m = int(input())
n = int(input())
sum =0
min_num = 10001
no_prime=0

for i in range(m,n+1):
    check = 0
    for j in range(2, i-1):
        if i % j == 0:
            check = 1
            no_prime = 1
            break
        else:
            pass

    if check == 0:
        sum+=i
        if min_num>i:
            min_num = i
print(no_prime)
if no_prime == 0:
    print('-1')
else:
    print(sum)
    print(min_num)
