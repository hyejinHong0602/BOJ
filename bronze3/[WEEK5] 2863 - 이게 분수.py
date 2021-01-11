a, b = map(int, input().split())
c, d = map(int, input().split())
m = [a/c+b/d, c/d+a/b, d/b+c/a, b/a+d/c]

large=m[0]
index=0

for i in range(4):
    if m[i]>large:
        large = m[i]
        index=m.index(m[i])

print(index)