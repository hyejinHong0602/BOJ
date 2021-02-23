n = int(input())
w_list=[]
res=0

for i in range(n):
    w = int(input())
    w_list.append(w)
w_list.sort(reverse=True)
for i in range(n):
    if res < w_list[i]*(i+1):
        res = w_list[i]*(i+1)

print(res)

# 가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게