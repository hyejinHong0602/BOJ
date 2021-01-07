# 이렇게 하면 런타임에러남.
while True:
    a, b = map(int, input().split())
    if (a>0 and b < 10):

        print(a+b)
    else:
        break

# 입력의 끝이 안정해져있기때문에 이렇게 except 처리를 해줘야한다고 한다.
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break