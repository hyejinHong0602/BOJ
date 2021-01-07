for i in range(3):
    a, b, c, d = map(int, input().split())
    if a+b+c+d==0: #윷
        print('D')
    elif a+b+c+d==1: #도
        print('C')
    elif a+b+c+d==2: #개
        print('B')
    elif a+b+c+d==3: #걸
        print('A')
    elif a+b+c+d==4: #모
        print('E')
