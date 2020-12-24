#2442 - 별찍기 5
# n = int(input())
#
# for i in range(1,n+1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))


#2443 - 별 찍기 6
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i)-1):
#         print("*",end='')
#     print()

#2444 - 별 찍기 7
# n=int(input())
# for i in range(0,n):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for k in range(2*i+1):
#         print("*", end='')
#     print()
# for i in range(1,n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i-1)+1):
#         print("*",end='')
#     print()

#2445 - 별 찍기 8
# n=int(input())
#
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end='')
#     for k in range(2 * (n - i)):
#         print(" ",end='')
#     for j in range(i):
#         print("*", end='')
#     print()
# for i in range(1,n):
#     for j in range(n-i):
#         print("*", end='')
#     for k in range(2 * i):
#         print(" ",end='')
#     for j in range(n-i):
#         print("*", end='')
#     print()

#2446 - 별 찍기 9
# n=int(input())
#
# for i in range(0,n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i-1)+1):
#         print("*",end='')
#     print()
#
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for k in range(2*i+1):
#         print("*", end='')
#     print()

#2455 - 지능형 기차
# M=0
# sum=0
# for i in range(4):
#     a, b=map(int, input().split())
#     sum-=a
#     sum+=b
#     if sum>M:
#         M=sum
# print(M)

#2460 - 지능형 기차2
# M=0
# sum=0
# for i in range(10):
#     a, b=map(int, input().split())
#     sum-=a
#     sum+=b
#     if sum>M:
#         M=sum
# print(M)

#2490 - 윷놀이
# for i in range(3):
#     a, b, c, d = map(int, input().split())
#     if a+b+c+d==0: #윷
#         print('D')
#     elif a+b+c+d==1: #도
#         print('C')
#     elif a+b+c+d==2: #개
#         print('B')
#     elif a+b+c+d==3: #걸
#         print('A')
#     elif a+b+c+d==4: #모
#         print('E')

#2506 - 점수계산
# n=int(input()) #문제 수
# t=list(map(int,input().split()))
# sum=0
# res=0
# for i in range(n):
#     if t[i]==1:
#         sum+=1
#         res+=sum
#     else:
#         sum=0
# print(res)

