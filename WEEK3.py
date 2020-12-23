#2442 - 별찍기 5
# n = int(input())
#
# for i in range(1,n+1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))


#2443 - 별 찍기 6
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i)-1):
#         print("*",end='')
#     print()

#2444 - 별 찍기 7
# n=int(input())
# for i in range(0,n):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for k in range(2*i+1):
#         print("*", end='')
#     print()
# for i in range(1,n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i-1)+1):
#         print("*",end='')
#     print()

#2445 - 별 찍기 8
# n=int(input())
#
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end='')
#     for k in range(2 * (n - i)):
#         print(" ",end='')
#     for j in range(i):
#         print("*", end='')
#     print()
# for i in range(1,n):
#     for j in range(n-i):
#         print("*", end='')
#     for k in range(2 * i):
#         print(" ",end='')
#     for j in range(n-i):
#         print("*", end='')
#     print()

#2446 - 별 찍기 9
# n=int(input())
#
# for i in range(0,n):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(2*(n-i-1)+1):
#         print("*",end='')
#     print()
#
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for k in range(2*i+1):
#         print("*", end='')
#     print()

