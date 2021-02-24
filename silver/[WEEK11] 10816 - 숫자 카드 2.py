import sys

n = int(sys.stdin.readline())
n_list = list(map(int, input().split()))

k = int(sys.stdin.readline())
k_list = list(map(int, input().split()))
n_list.sort()

dic = dict()

for i in n_list:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in k_list:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")

# for i in range(k):
#     print(n_list.count(k_list[i]), end=' ')
#


# count는 시간이 오래걸림.