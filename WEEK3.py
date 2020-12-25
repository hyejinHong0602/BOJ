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

#2511 - 카드놀이
# a_score=0
# b_score=0
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
#
# for i in range(10):
#     if a[i] > b[i]:
#         a_score += 3
#     elif a[i] < b[i]:
#         b_score += 3
#     else:
#         a_score += 1
#         b_score += 1
# print(a_score, b_score)
# if a_score > b_score :
#     print("A")
# elif a_score < b_score :
#     print("B")
# else:
#     print("D")
# a[i]=b[i]일때 코드 더 생각해봐야함.

#1316 - 그룹단어 체커
# n=int(input()) # 단어 개수
# res=0 # 그룹 단어 개수
# no_group=0 # 그룹단어인지 체크하기 위한 변수
#
# for i in range(n):
#     a = []  # 새로운 배열
#     word = input()
#     for j in range(len(word)-1):
#
#         if word[j] != word[j+1]:
#             if a.count(word[j]) == 0:  # 그룹 단어 아님
#                 a.append(word[j])
#                 if a.count(word[j+1]) == 0:
#                     a.append(word[j+1])
#                 else:
#                     no_group = 1
#             else:
#
#                 if a.count(word[j+1]) == 0:
#                     a.append(word[j+1])
#                 else:
#                     no_group = 1
#
#     if no_group==0: # no_group이 0이면 그룹단어이므로 결과값에 1 더해주기
#         res+=1
#     else:
#         no_group=0 # 다시 초기화 해주기
#
# print(res)

# 새로운 배열 a에 단어에서 연속되는 알파벳이 다른 부분을 체크해서 a에 들어갔는지 여부를 확인해서 없으면 넣고
# 들어가있으면 이미 나온 단어이므로 그룹 단어가 아닌 것이 되므로 no_group을 1로 설정해준다.


