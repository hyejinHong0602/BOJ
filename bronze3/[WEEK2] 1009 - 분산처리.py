# ---------------------이건 틀린 풀이
t=int(input())
for i in range(t):
    a, b = map(int, input().split())
    for i in range(b-1):
        a=a*a
    res=a%10
    if res==0:
        print(10)
    else:
        print(res)
# ----------------------
# 그냥 단순하게 자리수 별로 나누면서 한자리씩 구하려고 했지만 시간초과 등의 문제가 발생한다
# 이후 나머지를 이용하는 것이라는 것을 찾고 코드를 구현하였다.
# ---------------------
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)