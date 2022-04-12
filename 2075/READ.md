백준 2075번 N번째 큰 수
=======================

### <https://www.acmicpc.net/problem/2075>
<img width="868" alt="image" src="https://user-images.githubusercontent.com/83554018/162906885-ae2e2b78-1c91-4021-97ba-87823b6ceb5c.png">

<hr>

### 코드 설명
+ heapq 모듈 이용 -> min heap
+ heapify를 통해 root가 최소값이 되고, 한 줄씩 입력받으면서 n개만 남을때까지 최소값들을 제거해준다.
+ 따라서 n개가 남았을 때의 root가 n번째 큰 수가 된다.

### 소스코드
+ 메모리 : 32908 KB
+ 시간 : 832 ms
```python
import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(n-1):
    line = list(map(int, input().split()))
    for num in line:
        if heap[0] < num:
            heapq.heappushpop(heap, num)

print(heap[0])

```

### 오답 노트
+ 메모리 초과 - 조건 자체를 빡세게 준 것같다. heap 리스트 한 개를 제외하고 그 이상을 사용하면 무조건 메모리초과가 난다.
+ heap sort, max-heap 구현 등을 하려 했으나 메모리 초과가 난다.


### 오답 코드 - 메모리초과
```python
n = int(input())
heap = []

for _ in range(n):
    line = input().split()
    for num in line:
        heapq.heappush(heap, (-int(num), int(num)))

heap_sort = []

while len(heap_sort) < n:
    heap_sort.append(heapq.heappop(heap)[1])

print(heap_sort[-1])
```
