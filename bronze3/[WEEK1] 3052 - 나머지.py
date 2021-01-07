numbers=[] #숫자 10개 배열로 저장
index=[]
check=0
for i in range(10):
    numbers.append(int(input()))

for j in range(10):
    t=numbers[j]%42

    if len(index)==0:
        index.append(t)
    else:
        for k in range(len(index)):
            if index[k] == t:
                check=1
            else:
                continue
        if check==0:
            index.append(t)

print(len(index))
# 실행결과가 나오는데 답은 틀렸다고 해서 코드를 찾아보니 아래 코드가 나왔다.
# set 함수를 이용하면 간단하게 중복은 제거하고 arr에 넣을 수 있다.
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))