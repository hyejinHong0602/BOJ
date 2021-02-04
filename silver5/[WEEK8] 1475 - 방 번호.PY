n = input()
sixnine=0
others=0

for i in range(len(n)):
    if n[i]=='6' or n[i]=='9':
        sixnine+=1
    else:
        if others < n.count(n[i]):
            others = n.count(n[i])
if sixnine%2==1:
    sixnine=sixnine//2+1
elif sixnine%2==0:
    sixnine=sixnine//2

if sixnine < others:
    print(others)
else:
    print(sixnine)
