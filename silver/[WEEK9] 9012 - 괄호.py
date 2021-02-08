n = int(input())

for i in range(n):
    word = input()
    li = []
    check = 0 # 올바른 괄호 문자열(VPS)인지 확인
    # li랑 check 초기화 위치 잘 확인하기..
    for j in word[0:len(word)]:
        if len(li) > 0: # li에 요소가 있을 때
            if li[len(li) - 1] == j:
                li.append(j)
            else:
                if j == '(':
                    check = 1
                else:
                    li.pop()
        else: # li가 비어있을때
            if j == '(':
                li.append(j)
            else:
                check = 1
    if len(li) != 0: # 다했는데도 li에 요소 남아있으면 check
        check = 1

    if check == 1:
        print('NO')
    else:
        print('YES')
