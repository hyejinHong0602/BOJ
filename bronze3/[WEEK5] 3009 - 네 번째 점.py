a = []
b = []
for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

if a[0] != a[1]:
    if a[1] != a[2]:
        a.append(a[1])
    else:
        a.append(a[0])
else:
    a.append(a[2])

if b[0] != b[1]:
    if b[1] != b[2]:
        b.append(b[1])
    else:
        b.append(b[0])
else:
    b.append(b[2])

print(a[3], b[3])
