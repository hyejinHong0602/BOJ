numbers=[]
for i in range(9):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers))+1)
# ----------------------------------------#
numbers=[]
for i in range(9):
    numbers.append(int(input()))

max_num=numbers[0]

for j in range(9):
    if (max_num<numbers[j]):
        max_num=numbers[j]
        max_order=j+1
print(max_num)
print(max_order)
# 이렇게 한거는 런타임 에러 (최대값 100을 제한하지 못함)
