n = int(input())
member_list=[]

for i in range(n):
    age, name = map(str, input().split())
    age=int(age)
    member_list.append((age, name))

member_list.sort(key=lambda x : (x[0]))

for i in range(n):
    print(f'{member_list[i][0]} {member_list[i][1]}')
