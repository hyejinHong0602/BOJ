# m = int(input())
# n = int(input())
# sum_prime = 0
# prime = []
#
# for i in range(m, n + 1):
#     check = 0
#     if i != 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 check = 1
#                 break
#             else:
#                 pass
#     if check == 0:  # 소수임.
#         sum_prime += i
#         prime.append(i)
#
# if len(prime) == 0:
#     print('-1')
# else:
#     print(int(sum_prime))
#     print(int(prime[0]))

# 왜 자꾸 틀리는지 모르겠다.. 결과는 똑같이  나오는데 백준에서 틀렸다고 나옴.
M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
# 이걸로 제출했더니 맞음. 대체 위에거랑 뭐가 다른거지