s=[]

for i in range(5):
    a, b, c, d = map(int, input().split())
    s.append(a+b+c+d)

maximum = max(s)
print(s.index(maximum)+1, maximum)
