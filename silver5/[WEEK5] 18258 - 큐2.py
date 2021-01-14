import sys

queue = []
n = int(sys.stdin.readline())
cnt = 0  # rear의 index
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        try:
            print(queue[cnt])
            cnt += 1
        except:
            print('-1')
    elif command[0] == 'empty':
        if len(queue) == cnt:
            print('1')
        else:
            print('0')
    elif command[0] == 'size':
        print(len(queue) - cnt)
    elif command[0] == 'front':
        if len(queue) > cnt:
            print(queue[cnt])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(queue) > cnt:
            print(queue[len(queue) - 1])
        else:
            print('-1')

# 처음에 저번에 했던 큐대로 했었는데 시간초과가 나옴. 이유는 pop 연산 때문! pop 연산은 제거하고 하나씩 옮겨줘야하므로 시간이 오래걸림.
# -> 큐 내에서 pop대신 index를 사용하여 연산을 해줌으로써 해결.