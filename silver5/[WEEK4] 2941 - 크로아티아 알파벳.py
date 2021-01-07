list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()
for i in list:
    n = n.replace(i, '#')

print(len(n))
