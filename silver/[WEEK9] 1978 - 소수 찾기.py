n = int(input())
check = 0


number = list(map(int, input().split()))
for i in range(n):

    if number[i] != 1:
        tf = 0
        for j in range(2, number[i]):

            if number[i] % j == 0:
                tf = 1
                break
            else:
                continue

        if tf == 0:
            check += 1

    else:
        continue


print(check)