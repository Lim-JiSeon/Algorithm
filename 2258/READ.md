백준 2258번 정육점
=========================

### <https://www.acmicpc.net/problem/2258>
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/83554018/159341230-b88b8b1b-e198-4136-8ab5-aea6cf7291bf.png">

<hr>

### 코드 설명
+ 이 문제를 푸는데 고려해야 할 점이라면 같은 가격에 무게는 다른 고기가 있을 수도 있다는 점이다. 
+ 따라서 같은 가격일 때 되도록이면 무게가 더 무거운 고기를 먼저 택해 조건을 만족시키는 방향으로 코드를 짜야 한다.
+ 같은 가격일 때에는 고기를 무료로 얻을 수 있지 않기 때문에 더해주는 장치도 해야 한다.

### 소스코드
+ 메모리 : 54708 KB
+ 시간 : 400 ms
```python
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
meat = []
meat_weight = 0
pp = 0
ps = 0
minimum_cost = 3000000000
for _ in range(n):
    w, p = tuple(map(int, input().split()))
    meat.append((p,w))

meat.sort(key=lambda x:(x[0],-x[1]))

for p,w in meat:
    meat_weight += w
    if p > pp:
        ps = 0
        pp = p
    else:
        ps += p
    if meat_weight >= m:
        minimum_cost = min(minimum_cost, ps+p)

if meat_weight >= m:
    print(minimum_cost)
else:
    print(-1)
```

### 보충 노트
+ 선택한 가격보다 값이 작으면 무료로 고기를 얻을 수 있다는 조건에만 집중한 나머지 같은 가격일때를 전혀 고려해주지 않았다.
+ 가격을 기준으로 정렬하는 것은 맞았으나 오름차순으로 정렬한 뒤 뒤에서부터 확인작업을 해 앞에서부터 하는 것보다 복잡해졌다. -> 결국 수정
+ 문제를 제대로 읽지 않아 조건을 만족하지 않는다면 -1을 출력해줘야 한다는 점을 늦게 알았다.

### 틀렸습니다 - 같은 가격일때의 조건을 전혀 고려하지 않음

```python
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
meat = []
meat_weight = 0
minimum_cost = 3000000000
for _ in range(n):
    w, p = tuple(map(int, input().split()))
    meat.append((w,p))
    meat_weight += w

meat.sort(key = lambda x:x[1])

for i in range(n-1,0,-1):  
    if meat_weight >= m:
        if meat[i][1] == meat[i-1][1]:
            minimum_cost = min(minimum_cost, meat[i][1]+meat[i-1][1])
        else:
            minimum_cost = min(minimum_cost, meat[i][1])
    meat_weight -= meat[i][0]

if meat[0][0] >= m:
    print(meat[0][1])
else:
    print(minimum_cost)
```

### 틀렸습니다. - -1 출력 조건 고려하지 않음

```python
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
meat = []
meat_weight = 0
pp = 0
ps = 0
minimum_cost = 3000000000
for _ in range(n):
    w, p = tuple(map(int, input().split()))
    meat.append((p,w))

meat.sort(key=lambda x:(x[0],-x[1]))

for p,w in meat:
    meat_weight += w
    if p > pp:
        ps = 0
        pp = p
    else:
        ps += pp
    if meat_weight >= m:
        minimum_cost = min(minimum_cost, ps+p)

if meat[0][1] >= m:
    print(meat[0][0])
else:
    print(minimum_cost)
```

