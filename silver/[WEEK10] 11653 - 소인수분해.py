import sys
n = int(sys.stdin.readline())
prime_list = []

while n!=1:
    for j in range(2, n+1): # 이거 n+1이 아니라 n으로 해서 헤맴.
        if n % j == 0:
            n = n // j
            prime_list.append(j)
            break

for i in prime_list:
    print(i)

