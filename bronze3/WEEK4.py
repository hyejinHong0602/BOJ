# 2747 - 피보나치 수

# n=int(input())
# s=[0,1,]
#
# for i in range(2,n+1):
#     s.append(s[i-1]+s[i-2])
# print(s[n])


# 2754 - 학점계산

# dic = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
#        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
#        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
#        'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
#        'F': 0.0}
#
# grade=input()
#
# print(dic[grade])

# 2783 - 삼각 김밥

# x=[]
# y=[]
# a,b=map(int,input().split()) # 세븐 25의 삼각김밥 가격정보
# x.append(a)
# y.append(b)
# n=int(input()) # 세븐25를 제외한 편의점 개수
# cost=x[0]*1000/y[0]
#
# for i in range(n):
#     a,b=map(int,input().split())
#     x.append(a)
#     y.append(b)
#     cost_compare=x[i+1]*1000/y[i+1]
#     if cost > cost_compare:
#         cost=cost_compare
#
# print(cost)

