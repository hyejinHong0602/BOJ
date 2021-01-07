#2941 - 크로아티아 알파벳

# list=['c=','c-','dz=','d-','lj','nj','s=','z=']
# n=input()
# for i in list:
#     n=n.replace(i,'#')
#
# print(len(n))

#2751 - 수 정렬하기2
# x=[]
# n=int(input())
#
# for i in range(n):
#     a=int(input())
#     x.append(a)
#
#
# for i in range(n):
#     for j in range(n-i-1):
#         if x[j] > x[j+1]:
#             x[j], x[j+1]=x[j+1],x[j]
#
# for i in range(n):
#     print(x[i])

# 시간초과 -> 삽입정렬 O(N^2)
# import sys
# n = int(input())
# x = []
# for i in range(n):
#     a=int(input())
#     x.append(a)
#
# x=sorted(x)
#
# for i in range(len(x)):
#     print(x[i])
# 내장함수 sorted 이용 -> O(nlogn)

# import sys
# n = int(sys.stdin.readline())
# a = sorted(list(map(int,sys.stdin.read().split())))
# print('\n'.join(map(str,a)))
## 검색해본 코드

#2748 - 피보나치수2

# n=int(input())
# s=[0,1,]
#
# for i in range(2,n+1):
#     s.append(s[i-1]+s[i-2])
# print(s[n])

#2609
# x, y = map(int, input().split())
# s = x * y
#
# if y > x:
#     x, y = y, x  # 큰수, 작은수 판단
#
# while True:
#     mod = x % y
#     if mod != 0:
#         x = y
#         y = mod
#     else:
#         a = y # 최대공약수 a
#         break
#
# print(a)
# print(s//a) # 최소공배수 s//a
#
# # 유클리드 호제법 이용
# # 최대공약수는 큰수를 작은수로 나눈 mod값을 구하고 나눴던 값을 mod 값으로 나누고를 mod 값이 0이 될때까지 반복
# # 최소공배수는 원래있던 x와 y를 곱한값에서 최대공약수로 나눠주면 나옴
