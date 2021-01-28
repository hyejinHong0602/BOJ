from typing import MutableSequence

# def shell_sort(a:MutableSequence) -> None:
#     n=len(a)
#     h=n//2
#     while h>0:
#         for i in range(h,n):
#             j=i-h
#             tmp = a[i]
#             while j>=0 and a[j]>tmp:
#                 a[j+h] = a[j]
#                 j-=h
#             a[j+h]=tmp
#         h//=2

# h 값이 서로 배수가되지 않도록 해야 원소가 충분히 뒤섞여 효율 좋은 정렬을 기대할 수 있음.
# 121 - 40 - 13 - 4 - 1 .. 이런 수열을 사용하면 셸 정렬 알고리즘을 간단하게 만들 수 있고
# 효율적인 정렬 가능. 1부터 시작하여 3배한 값에 1을 더하고 있음. 하지만 h의 초기값이 지나치게 크면 효과 없ㅇ,ㅁ.
# 배열의 원소 수인 n을 9로 나누었을 때 그 몫을 넘지 않도록 정해야함.

def shell_sort(a: MutableSequence)-> None:
    n=len(a)
    h=1

    while h<n//9:
        h=h*3+1

    while h>0:
        for i in range(h, n):
            j=i-h
            tmp=a[i]
            while j>=0 and a[j]>tmp:
                a[j+h]=a[j]
                j-=h
            a[j+h]=tmp
        h//=3



if __name__=='__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x=[None] * num

    for i in range(num):
        x[i]=int(input(f'x[{i}]: '))

    shell_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 셸 정렬의 시간복잡도는 O(n^1.25)이고 단순 정렬의 시간 복잡도인 O(n^2)보다 매우 빠름.
# but, 안정적이지 않음.