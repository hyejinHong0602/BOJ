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
#
## 시간초과 -> 삽입정렬 O(N^2)

import sys

n = int(input())
x = []
for i in range(n):
    a = int(input())
    x.append(a)

x = sorted(x)

for i in range(len(x)):
    print(x[i])
# 내장함수 sorted 이용 -> O(nlogn)

# import sys
# n = int(sys.stdin.readline())
# a = sorted(list(map(int,sys.stdin.read().split())))
# print('\n'.join(map(str,a)))
## 검색해본 코드
