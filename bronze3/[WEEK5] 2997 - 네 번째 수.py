a, b, c = map(int,input().split())
s=[a,b,c]
sorted_s=sorted(s)


if sorted_s[1]-sorted_s[0]==sorted_s[2]-sorted_s[1]:
    print(sorted_s[2]+sorted_s[2]-sorted_s[1])
elif sorted_s[1]-sorted_s[0] > sorted_s[2]-sorted_s[1]:
    print((sorted_s[1]+sorted_s[0])//2)
else:
    print((sorted_s[2] + sorted_s[1]) // 2)