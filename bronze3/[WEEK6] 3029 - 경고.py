import sys

a = input().split(':')
b = input().split(':')
c = [int(b[0]) - int(a[0]), int(b[1]) - int(a[1]), int(b[2]) - int(a[2])]

if c[0] < 0:
    c[0] = c[0] + 24


for i in range(2,0,-1):
    if c[i] < 0:
        c[i] = c[i] + 60
        c[i-1]=c[i-1]-1

if c[0]==0 and c[2]==0 and c[2]==0:
    c[0]=24

for i in range(3):
    if c[i] < 10:
        c[i] = f'0{c[i]}'


print(f'{c[0]}:{c[1]}:{c[2]}')

