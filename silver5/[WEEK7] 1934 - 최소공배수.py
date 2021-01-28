n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a
    multiple_ab = a * b

    mod = b % a
    while mod != 0: 
        if mod != 0:
            b = a
            a = mod
            mod = b % a


    gcd = a
    print(multiple_ab // gcd)
    # 최소공배수
