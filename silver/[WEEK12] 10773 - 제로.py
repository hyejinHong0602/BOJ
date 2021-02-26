n = int(input())
a_list=[]
for i in range(n):
    a = int(input())
    if a !=0:
        a_list.append(a)
    else:
        a_list.pop()

print(sum(a_list))