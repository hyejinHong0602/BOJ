T = int(input())


for i in range(T):
    sumEven = 0
    minEven = 100
    nums = list(map(int, input().split()))
    for j in range(len(nums)):
        if nums[j]%2==0: #짝수
            sumEven+=nums[j]
            if nums[j]<minEven:
                minEven=nums[j]

    print(f'{sumEven} {minEven}')
