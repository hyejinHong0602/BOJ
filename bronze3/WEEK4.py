
1316 - 그룹단어 체커
n=int(input()) # 단어 개수
res=0 # 그룹 단어 개수
no_group=0 # 그룹단어인지 체크하기 위한 변수

for i in range(n):
    a = []  # 새로운 배열
    word = input()
    for j in range(len(word)-1):

        if word[j] != word[j+1]:
            if a.count(word[j]) == 0:  # 그룹 단어 아님
                a.append(word[j])
                if a.count(word[j+1]) == 0:
                    a.append(word[j+1])
                else:
                    no_group = 1
            else:

                if a.count(word[j+1]) == 0:
                    a.append(word[j+1])
                else:
                    no_group = 1

    if no_group==0: # no_group이 0이면 그룹단어이므로 결과값에 1 더해주기
        res+=1
    else:
        no_group=0 # 다시 초기화 해주기

print(res)

새로운 배열 a에 단어에서 연속되는 알파벳이 다른 부분을 체크해서 a에 들어갔는지 여부를 확인해서 없으면 넣고
들어가있으면 이미 나온 단어이므로 그룹 단어가 아닌 것이 되므로 no_group을 1로 설정해준다.


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

