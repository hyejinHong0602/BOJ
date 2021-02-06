# import sys
#
# stack=[]
# n=int(sys.stdin.readline())
# cnt=1
# for i in range(n):
#     h=int(sys.stdin.readline())
#     stack.append(h)
#
# for i in range(n-1):
#     if stack[i] > stack[n-1]:
#         cnt += 1
#
# print(cnt)
# 처음에 생각했을 때 단순하게 마지막 막대보다 크면 보이는 줄 알고 그렇게 했더니 실패가 나왔다.
# 하지만 그게아니라 오른쪽에 자신보다 같거나 큰 막대가 있으면 보이지 않는것이다.

import sys

stack = []
n = int(sys.stdin.readline())

for i in range(n):
    h = int(sys.stdin.readline())
    if i == 0:
        stack.append(h)
    else:
        if max(stack) < h:
            stack.clear()
            stack.append(h)
        else:
            if stack[len(stack) - 1] > h:
                stack.append(h)
            else:
                while stack[len(stack) - 1] <= h:
                    stack.pop()
                stack.append(h)

print(len(stack))

# 백준에 정답을 입력했을 때 런타임에러(indexerror)라고 뜨는데 왜그러는지 모르겠음. 무한루프 때문인 거 같은데 아직 해결 못했음.