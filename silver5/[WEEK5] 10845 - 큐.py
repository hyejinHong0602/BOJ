import sys

def push(x):
    queue.append(x)

def pop():
    try:
        print(queue.pop(0))
    except:
        print('-1')

def size():
    print(len(queue))

def empty():
    if len(queue)==0:
        print('1')
    else:
        print('0')

def front():
    try:
        print(queue[0])
    except:
        print('-1')

def back():
    try:
        print(queue[len(queue)-1])
    except:
        print('-1')

queue=[]
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        push(command[1])
    elif command[0]=='pop':
        pop()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'size':
        size()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
