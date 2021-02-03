import pandas as pd  # 패키지는 다 설치되어 있다고 가정
import numpy as np
import seaborn as sns

# 문제 1
# midterm = [34, 30, 26, 40, 33, 15, 31, 21, 17, 40]
# finalterm = [45, 48, 25, 50, 50, 28, 39, 33, 47, 42]
# hw = [5, 10, 8, 10, 10, 7, 7, 9, 10, 2]
# score=[]
# for n, v, c in zip(midterm, finalterm, hw):
#     score.append(n+v+c)
#
# score.sort()
# score.reverse()
# print(score)

# info = []
# sn = input('지원번호를 입력하세요: ')
#
# year = int(sn[0:2]) * 2
#
# sn = list(sn)
#
# if sn[2] == '1':
#     year = year + 1 - 36
#     info.append(year)
# else:
#     year = year - 36
#     info.append(year)
#
# if sn[3] == '1':
#     info.append('남')
#     info.append('x')
# elif sn[3] == '2':
#     info.append('여')
#     info.append('x')
# elif sn[3] == '3':
#     info.append('남')
#     info.append('o')
#     info[0] = info[0] - 1
# elif sn[3] == '4':
#     info.append('여')
#     info.append('o')
#     info[0] = info[0] - 1
#
#
# if sn[len(sn)-1] == 's':
#     info.append('o')
# else:
#     info.append('x')
#
# print(f'성별: {info[1]}')
# print(f'기수: {info[0]}')
# print(f'편입: {info[2]}')
# print(f'운영진: {info[3]}')

