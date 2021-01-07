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

# 새로운 배열 a에 단어에서 연속되는 알파벳이 다른 부분을 체크해서 a에 들어갔는지 여부를 확인해서 없으면 넣고
# 들어가있으면 이미 나온 단어이므로 그룹 단어가 아닌 것이 되므로 no_group을 1로 설정해준다.
