n = int(input())

cnt=0
while n!=0:
    if n % 2 == 1:
        cnt += 1
    n=n//2
print(cnt)

# 10진수를 2진수로 바꿨을 때 1이 몇개가 있냐는 문제