List = ['-','\\','(','@','?','>','&','%']
while True:
  N = list(input())
  if N[0] =='#':
      break
  for i in range(len(N)):
     for j in List:
       if N[i] == j :
         N[i] = List.index(j)
       elif N[i] == '/' :
          N[i] = -1
  A = 0

  for i in range(len(N)):
    A += N[i]*(8**(len(N)-1-i))
  print(A)
