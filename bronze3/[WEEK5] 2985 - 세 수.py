a, b, c = map(int, input().split())

if a+b==c:
    print(f'{a}+{b}={c}')
elif a-b==c:
    print(f'{a}-{b}={c}')
elif a*b==c:
    print(f'{a}*{b}={c}')
elif a / b == c:
    print(f'{a}/{b}={c}')
elif a==b+c:
    print(f'{a}={b}+{c}')
elif a==b-c:
    print(f'{a}={b}-{c}')
elif a==b*c:
    print(f'{a}={b}*{c}')
elif a == b / c:
    print(f'{a}={b}/{c}')
# 등호가 a랑 b 사이에 있을 때 & b랑 c 사이에 있을 때