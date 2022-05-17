백준 19942번 다이어트
======================

### <https://www.acmicpc.net/problem/19942>
<img width="879" alt="image" src="https://user-images.githubusercontent.com/83554018/168798970-c560a599-d875-4c1a-8c8a-ac49911660f2.png">

<hr>

### 코드 설명
+ combination을 이용해서 조합을 모두 구한 뒤 for문을 돌리면서 가격이 최소가 되는 조합을 찾는다.
+ 추가적으로 최소 가격이 같은 조합이 여러 개 일때에는 사전 순으로 정렬한 뒤 가장 앞에 있는 조합을 리턴해야 함으로 장치를 해준다.
+ 주의해야 할 점은 인덱스는 0부터 돌아가기 때문에 조합을 구할 때에는 인덱스로 했지만 문제에서는 1번째부터라고 되어 있기 때문에 인덱스 값에 1씩 더한 값을 출력해야 한다.  

### 소스코드
+ 메모리 : 32952 KB
+ 시간 : 220 ms
```python
import sys, math
from itertools import combinations

input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]
min_cost = math.inf
answer = []

for cnt in range(1, n+1):
    for pair in combinations(list(range(n)), cnt):
        p,f,s,v,c = 0,0,0,0,0
        for idx in pair:
            p += ingredients[idx][0]
            f += ingredients[idx][1]
            s += ingredients[idx][2]
            v += ingredients[idx][3]
            c += ingredients[idx][4]
        
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if min_cost > c:
                min_cost = c
                answer = list(pair)
            elif min_cost == c:
                answer = sorted((answer,list(pair)))[0]

if min_cost == math.inf:
    print(-1)
else:
    print(min_cost)
    for a in answer:
        print(a+1, end=" ")

```
