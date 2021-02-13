n = int(input())
prime_list = []

while True:
    for i in range(2, n):
        if n % i == 0:
            n = n // i
            prime_list.append(i)
            break



