#10818번
# n=int(input())
# numbers=list(map(int,input().split()))
#
# max_num=numbers[0]
# min_num=numbers[0]
#
# for i in range (n) :
#     if (max_num < numbers[i]):
#         max_num=numbers[i]
#     if (min_num > numbers[i]):
#         min_num=numbers[i]
#
# print(min_num, max_num)

#2562번
# numbers=[]
# for i in range(9):
#     numbers.append(int(input()))
#
# print(max(numbers))
# print(numbers.index(max(numbers))+1)
#----------------------------------------#
# numbers=[]
# for i in range(9):
#     numbers.append(int(input()))
#
# max_num=numbers[0]
#
# for j in range(9):
#     if (max_num<numbers[j]):
#         max_num=numbers[j]
#         max_order=j+1
# print(max_num)
# print(max_order)
#이렇게 한거는 런타임 에러 (최대값 100을 제한하지 못함)

#2438번
# n=int(input('n='))
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

#2739번
# n=int(input())
# for i in range(1,10):
#     print(f'{n} * {i} = {n*i}')

#2741번
# n=int(input())
# for i in range(1,n+1):
#     print(i)

#2742번
# n=int(input())
# for i in range(1,n+1):
#     print(n+1-i)

#2439번
# n=int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(i):
#         print('*',end='')
#     print()

#10871번
# n,x =map(int, input().split())
#
# a=list(map(int, input().split())) #다시 체크하기
#
# for j in range(n):
#     if a[j]<x:
#         print(a[j], end=' ')

#10817번
# a,b,c =map(int,input().split())
# mid=a
# if a>=b:
#     if b>=c:
#         mid = b
#     elif a<=c:
#         mid = a
#     else:
#         mid=c
# else:
#     if b<=c:
#         mid=b
#     elif a>=c:
#         mid=a
#     else:
#         mid=c
#
# print(mid)

#10950번
# t=int(input())
# sum=[]
# for i in range(t):
#     a,b=map(int,input().split())
#     sum.append(a+b)
#
# for j in range(t):
#     print(sum[j])

#10952번
# while True:
#     a, b = map(int, input().split())
#     if (a!=0 and b!=0):
#         print(a+b)
#     else:
#         break

#2440번
# n=int(input())
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     print()

#11021번
# t=int(input())
#
# sum=[]
# for i in range(t):
#     a, b = map(int, input().split())
#     sum.append(a+b)
#
# for j in range(t):
#     print(f'Case #{j+1}: {sum[j]}')

# 2441번
# n=int(input())
#
# for i in range(n):
#     for k in range(i):
#         print(' ',end='');
#     for j in range(n-i):
#         print('*',end='')
#     print()

#11022번
# t=int(input())
#
# for i in range(t):
#     a, b = map(int, input().split())
#     print(f'Case #{i + 1}: {a} + {b} = {a+b}')

#10951번

# 이렇게 하면 런타임에러남.
# while True:
#     a, b = map(int, input().split())
#     if (a>0 and b < 10):
#
#         print(a+b)
#     else:
#         break

# 입력의 끝이 안정해져있기때문에 이렇게 except 처리를 해줘야한다고 한다.
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

#10818
# n=int(input())
#
# a=list(map(int,input().split()))
# max=a[0]
# min=a[0]
#
# for i in range(n):
#     if a[i]>max:
#         max=a[i]
#     if a[i]<min:
#         min=a[i]
#
# print(min, max)

#11718번 이것도 eof
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break