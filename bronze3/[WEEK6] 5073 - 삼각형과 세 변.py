a=1
b=1
c=1

while a!=0 or b!=0 or c!=0:
    a, b, c = map(int, input().split())
    nums=[a,b,c]
    sortedNum=sorted(nums)

    if sortedNum[2] >= sortedNum[1]+sortedNum[0]:
        if a == 0 and b == 0 and c == 0:
            pass
        else:
            print('Invalid')
    else:
        if a == b:
            if b == c:
                 print('Equilateral')
            else:
                print('Isosceles')
        else:
            if b == c:
                print('Isosceles')
            else:
                if a == c:
                    print('Isosceles')
                else:
                    print('Scalene')


