# n = int(input())
# nlist=[]
# for i in range(1,n+1):
#     nlist.append(i)
#
#
# while len(nlist)!=1:
#     nlist.pop(0)
#     nlist.append(nlist[0])
#     nlist.pop(0)
#
#
# print(nlist[0])
# 시간 초과 -> collection.deque 써야함.

import sys
import collections

n = int(sys.stdin.readline())
queue=[]
queue=collections.deque([i for i in range(1,n+1)])

while len(queue)!=1:
    queue.popleft()
    num=queue.popleft()
    queue.append(num)

print(queue[0])