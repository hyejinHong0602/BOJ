import sys
a = sys.stdin.readline()
command = list(a)
ball=[1,0,0]

for i in range(len(command)-1):
    if command[i]=='A':
        ball[0], ball[1] = ball[1], ball[0]
    elif command[i] == 'B':
        ball[1], ball[2] = ball[2],ball[1]
    elif command[i] == 'C':
        ball[0], ball[2] = ball[2],ball[0]
if ball.index(1)==0:
    res=1
elif ball.index(1)==1:
    res=2
elif ball.index(1)==2:
    res=3

print(res)
