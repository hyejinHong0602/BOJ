#교재 실습

# print('세 정수의 최대값을 구합니다')
# a=int(input('정수 a값을 입력하세요:'))
# b=int(input('정수 b값을 입력하세요.'))
# c=int(input('정수 c값을 입력하세요.'))
#
# maximum=a
# if b>maximum : maximum=b
# if c>maximum : maximum=c
# print(maximum)

# def max3(a,b,c):
#     maximum=a;
#     if b>maximum:maximum=b
#     if c>maximum:maximum=c
#     return maximum
#
# print(f'최대값은?={max3(3,2,5)}')

#-----#
# name=input('이름을 입력하세요:')
# print(f'안녕하세요? {name} 님.')

#-----#
#중앙값 구하기

# def med3(a,b,c):
#     if a>=b:
#         if b>c:
#             return b
#         elif a<=c:
#             return a
#         else:
#             return c
#     elif a>c:
#         return a
#     elif b>c:
#         return c
#     else:
#         return b
#
#
# print(f'중앙값: {med3(2,7,3)}')
# print(f'중앙값: {med3(7,2,3)}')
# print(f'중앙값: {med3(1,3,6)}')

#a부터 b까지의 합 구하기

# def sum2(a,b):
#     if a>b:
#         a,b=b,a
#     sum=0
#
#     for i in range(a, b+1):
#         sum+=i
#
#
# print(f'합? {sum2(2,4)}')

# n=int(input('몇개를 출력?'))
#
# for i in range(1,n+1):
#     if (i % 2 == 1):
#         print(f'+', end='')
#     else:
#         print(f'-', end='')


# num=int(input('몇개출력?'))
# cut=int(input('몇개마다?'))
#
# for i in range(1, num + 1):
#     print(f'*', end='')
#     if i % cut == 0:
#         print()
#
#for문 마다 if문을 수행하는건 효율적이지 않음.
# num=int(input('몇개출력?'))
# cut=int(input('몇개마다?'))
#
# n=num//cut
# nrest=num%cut
# for i in range(n):
#     print('*'*cut,end='')
#     print()
# for j in range(nrest):
#     print('*',end='')

# s=int(input('넓이:'))
#
# for i in range(1,s):
#     if i*i>s:break #중복제한
#     if s%i==0:
#         print(i,s//i)
