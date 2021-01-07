x, y = map(int, input().split())
s = x * y

if y > x:
    x, y = y, x  # 큰수, 작은수 판단

while True:
    mod = x % y
    if mod != 0:
        x = y
        y = mod
    else:
        a = y # 최대공약수 a
        break

print(a)
print(s//a) # 최소공배수 s//a

# 유클리드 호제법 이용
# 최대공약수는 큰수를 작은수로 나눈 mod 값을 구하고 나눴던 값을 mod 값으로 나누고를 mod 값이 0이 될때까지 반복
# 최소공배수는 원래있던 x와 y를 곱한값에서 최대공약수로 나눠주면 나옴
