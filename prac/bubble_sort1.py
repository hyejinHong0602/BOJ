from typing import MutableSequence

# def bubble_sort(a:MutableSequence) -> None:
#     n=len(a)
#     for i in range(n-1):
#         for j in range(n-1, i, -1):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
# 개선전 버블 정렬

# def bubble_sort(a:MutableSequence) -> None:
#     n=len(a)
#     for i in range(n-1):
#         exchange=0
#         for j in range(n-1, i, -1):
#             if a[j-1]>a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 exchange+=1
#         if exchange==0:
#             break
# 교환 횟수에 따라 중단 방식을 적용하여 개선한 프로그램 (개선 1)
# 마지막 패스를 종료한 시점에서 exchange 값이 0이면 정렬을 마친것으로 break문에 의해
# 바깥쪽 for문을 강제로 탈출하고 함수실행을 종료함.

def bubble_sort(a : MutableSequence) -> None:
    n = len(a)
    k=0
    while k<n-1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1]>a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k=last
# 이미 정렬된 원소를 제외한 나머지만 비교, 교환할 수 있도록 스캔 범위를 제한하는 방법으로 개선한 프로그램 (개선 2)
# 새로운 변수 last는 각 패스에서 마지막으로 교환한 두 원소 가우데 오른쪽 원소인 a[j] 인덱스를 저장.
# 교환할 때마다 오른쪽 원소의 인덱스 값을 last에 대입.
# 하나의 패스를 마친 시점에 last의 값을 k에 대입하여 다음에 수행할 패스의 스캔 범위를 a[k]로 제한
# 그러면 다음 패스에서 마지막으로 비교할 두 원소는 a[k]와 a[k+1]이다.

if __name__=='__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x= [None] * num # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')