while True:
  leef = 1
  case = list(map(int, input().split()))
  if str(case[0]) != '0':
    for i in range(1,case[0]+1):
      leef *= case[2*i-1]
      leef -= case[2*i] #가지치기
    print(leef)
  else:
      break
