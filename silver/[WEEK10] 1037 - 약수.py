num = int(input())

a = list(map(int,input().split()))
amax = max(a)
amin = min(a)
print(amax * amin)