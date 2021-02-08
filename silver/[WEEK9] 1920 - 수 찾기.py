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


n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    if BinarySearch(a, b[i], 0, n - 1):
        print('1')
    else:
        print('0')

# 그냥 b[i] in a를 썼을 때 시간초과
# 그래서 이진탐색 이용
