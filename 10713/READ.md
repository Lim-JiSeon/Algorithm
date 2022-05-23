백준 10713번 기차 여행
======================

### <https://www.acmicpc.net/problem/10713>
<img width="884" alt="image" src="https://user-images.githubusercontent.com/83554018/169882155-70577106-9a82-4e7b-aecd-79020ee25038.png">

<hr>

### 코드 설명
+ 여행하기로 한 도시들을 방문하는데 이용하는 철도들의 이용 빈도를 세는 것이 이 문제의 핵심 포인트이다.
+ 최소 비용은 A에 빈도를 곱한 값과 B에 빈도를 곱하고 C를 더한 값 둘 중에 최소값들의 합이다.
+ 철도마다 1씩 더해주는 방식으로 하면 N^2이 나오기 때문에 시간초과난다.
+ 철도는 양방향이기 때문에 A -> B 와 B -> A는 같은 철도를 이용한 것이다. 
+ 양방향인 점을 이용해서 두 도시 번호 중 작은 값을 출발로 취급하고 큰 값을 도착으로 취급해 계산한다.(반대로 해도 상관없음)
+ 출발 도시 번호에는 1씩 더해주고 도착 도시 번호에는 -1씩 더해준다. -> 출발지점과 도착지점만 표시
+ prefix sum 구간합을 구해 배열에 넣어준다.

### 소스코드
+ 메모리 : 60744 KB
+ 시간 : 444 ms
```python
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
p = list(map(int, input().split()))
cost = [list(map(int, input().split())) for _ in range(n-1)]
freq = [0 for _ in range(n)]
min_cost = 0

for idx in range(m-1):
    s, e = min(p[idx], p[idx+1]), max(p[idx], p[idx+1])
    freq[s-1] += 1
    freq[e-1] -= 1

for idx in range(1,n):
    freq[idx] = freq[idx-1] + freq[idx]

for idx in range(n-1):
    if freq[idx] > 0:
        min_cost += min(freq[idx]*cost[idx][0], freq[idx]*cost[idx][1] + cost[idx][2])

print(min_cost)
```
