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
