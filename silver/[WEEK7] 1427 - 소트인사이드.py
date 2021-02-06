n =input()
n_list = list(n)
idx=len(n_list)

n_sort=sorted(n_list)
for i in range(idx-1, -1, -1):
    print(n_sort[i],end='')