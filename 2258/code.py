import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
meat = []                                             # 무게와 가격을 입력받아 저장할 리스트
meat_weight = 0                                       # 무게의 총 합
pp = 0                                                # 이전 가격
ps = 0                                                # 이전 가격들의 합
minimum_cost = 3000000000                             # 최소 가격
for _ in range(n):
    w, p = tuple(map(int, input().split()))
    meat.append((p,w))                                # (가격, 무게) 형식으로 append
    
meat.sort(key=lambda x:(x[0],-x[1]))                  # x[0]을 기준으로 정렬하되 그 값이 같으면, x[-1]은 반대로 정렬

for p,w in meat:
    meat_weight += w
    if p > pp:                                        # 가격이 같을 수도 있기 때문에 구분해서 생각
        ps = 0                          
        pp = p
    else:                                             # 가격이 같을 경우로, 이전 가격의 합에 현재 가격을 더해줌(현재가격과 이전가격이 같기 때문에 이전 가격을 더해주는 것과 다름없음)
        ps += p
    if meat_weight >= m:                              # 조건을 만족하면 최소가격 초기화 해주기
        minimum_cost = min(minimum_cost, ps+p)

if meat_weight >= m:
    print(minimum_cost)
else:                                                 # 조건을 만족 못할 수도 있기 때문에 그럴 경우 -1 리턴
    print(-1)
