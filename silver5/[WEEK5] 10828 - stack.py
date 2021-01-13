import sys
def push(x):
    stack.append(x)

def pop():
    try:
        print(stack.pop())
    except:
        print('-1')

def empty():
    if len(stack)==0:
        print('1')
    else:
        print('0')

def size():
    print(len(stack))

def top():
    try:
        print(stack[len(stack) - 1])
    except:
        print('-1')


stack=[]
# n=int(input())
n= int(sys.stdin.readline())

for i in range(n):
    # num = input().split()
    command = sys.stdin.readline().split()

    if command[0]=='push':
        push(command[1])
    elif command[0]=='pop':
        pop()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'size':
        size()
    elif command[0] == 'top':
        top()

# 시간초과가 계속 나와서 찾아보고 sys.stdin.readline()으로 고쳤더니 해결.