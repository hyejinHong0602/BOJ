#1009 - 분산처리
#---------------------이건 틀린 풀이
# t=int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     for i in range(b-1):
#         a=a*a
#     res=a%10
#     if res==0:
#         print(10)
#     else:
#         print(res)
#----------------------
#그냥 단순하게 자리수 별로 나누면서 한자리씩 구하려고 했지만 시간초과 등의 문제가 발생한다
#이후 나머지를 이용하는 것이라는 것을 찾고 코드를 구혀하였다.
# ---------------------
# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     a = a % 10
#
#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a * a) % 10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a ** 4) % 10 % 10 % 10)
#         else:
#             print((a ** b) % 10 % 10 % 10)
#
#1284 - 집주소
#
# while True:
#     sum = 2
#     n = int(input())
#
#     while n>=10:
#
#         if n%10==1:
#             sum=sum+2
#         elif n%10==0:
#             sum=sum+4
#         else:
#             sum=sum+3
#         n=n//10
#         sum = sum + 1
#
#
#     if n % 10 == 1:
#         sum = sum + 2
#     elif n % 10 == 0:
#         sum = sum + 4
#     else:
#         sum = sum + 3
#
#
#
#     if n==0:
#         break
#     print(sum)
#
#1이면 2cm
#0이면 4cm
#나머지는 3cm

#1547
# m=int(input())
# c=[0,1,0,0]
# for i in range(m):
#     x, y=map(int,input().split())
#     c[x],c[y]=c[y],c[x]
# print(c.index(1))

#2010

# n = int(input())
# sum = 0
# for i in range(n):
#     t=int(input())
#     sum += t
# print(sum - (n - 1))

#2163
# n, m = map(int, input().split())
# print(n*m-1)

#2443 - 별 찍기6
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i)-1):
#         print("*",end='')
#     print()
