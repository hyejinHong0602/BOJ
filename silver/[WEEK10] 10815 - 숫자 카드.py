# import sys
#
# n = int(sys.stdin.readline())
# nlist = list(map(int, input().split()))
#
# m = int(sys.stdin.readline())
# mlist= list(map(int, input().split()))
#
# for i in mlist:
#     if i in nlist:
#         print('1', end = ' ')
#     else:
#         print('0', end = ' ')

# 시간 초과 -> 이분 탐색


import sys


def BinarySearch(arr, num, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] > num:
        return BinarySearch(arr, num, low, mid - 1)
    elif arr[mid] < num:
        return BinarySearch(arr, num, mid + 1, high)
    else:
        return True


n = int(sys.stdin.readline())
nlist = list(map(int, input().split()))
nlist=sorted(nlist) # 필수!

m = int(sys.stdin.readline())
mlist = list(map(int, input().split()))

for i in range(m):
    if BinarySearch(nlist, mlist[i], 0, n - 1):
        print('1', end=' ')
    else:
        print('0', end=' ')

# 이분탐색시 꼭 정렬된 배열에서 해야하는거 까먹지 말기!