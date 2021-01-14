import sys

deque = []
n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deque.insert(0, command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'pop_front':
        try:
            print(deque.pop(0))
        except:
            print('-1')
    elif command[0] == 'pop_back':
        try:
            print(deque.pop())
        except:
            print('-1')
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque)==0:
            print('1')
        else:
            print('0')
    elif command[0] == 'front':
        try:
            print(deque[0])
        except:
            print('-1')
    elif command[0] == 'back':
        try:
            print(deque[len(deque)-1])
        except:
            print('-1')






