# a_score=0
# b_score=0
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
#
# for i in range(10):
#     if a[i] > b[i]:
#         a_score += 3
#     elif a[i] < b[i]:
#         b_score += 3
#     else:
#         a_score += 1
#         b_score += 1
# print(a_score, b_score)
# if a_score > b_score :
#     print("A")
# elif a_score < b_score :
#     print("B")
# else:
#     print("D")
# ## a[i]=b[i]일때 코드 더 생각해봐야함.

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
state=''
for i in range(10):
    a,b = A[i],B[i]
    if a>b:
        state += 'A'
    elif a<b:
        state += 'B'
    else:
        state += 'D'

equal = state.count('D')
total_A = state.count('A')*3 + equal
total_B = state.count('B')*3 + equal
print(total_A, total_B)

if total_A == total_B:
    final_state = state.replace('D','')
    if len(final_state) != 0:
        print(state.replace('D','')[-1])
    else:
        print('D')
elif total_A > total_B : print('A')
else : print('B')

