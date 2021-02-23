import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = []
sum = 0

for i in range(n):
    a = int(sys.stdin.readline())
    n_list.append(a)
    sum += a
print(round(sum / n))  # 산술평균

n_list.sort()
print(n_list[(n - 1) // 2])  # 중앙값

# 최빈값 구하는게 까다로웠음
count = Counter(n_list).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(n_list[n - 1] - n_list[0])  # 범위
