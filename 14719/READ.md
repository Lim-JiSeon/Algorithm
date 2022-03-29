백준 14719번 빗물
==================

### <https://www.acmicpc.net/problem/14719>
<img width="885" alt="image" src="https://user-images.githubusercontent.com/83554018/160583950-776dc7be-0051-4547-b0c2-e5d21a0304e3.png">

<hr>

### 코드 설명
+ 직관적으로 blocks 라는 이차원 배열을 만들어서 해결했다. 
+ 벽은 1로, 빈 공간은 0으로 표시를 한 뒤 위에서부터 가로 방향으로 검사를 하면서 1을 만나면 c1을 그 인덱스 위치로 초기화 해준 뒤 또 1을 만나면 c2를 인덱스로 초기화해 두 간격을 계산했다.
+ 이중 for문으로 간단하게 해결할 수 있는 문제였으나 더 효율적으로도 해결이 가능하다. -> 변수와 높이 차 이용

### 소스코드
+ 메모리 : 30988 KB
+ 시간 : 120 ms
```python
import sys
input = sys.stdin.readline

h, w = tuple(map(int, input().split()))
heights = list(map(int, input().split()))
blocks = [[0]*w for _ in range(h)]
answer = 0

for i in range(w):
    for j in range(h-1,h-heights[i]-1,-1):
        blocks[j][i] = 1
    
for i in range(h):
    c1, c2 = -1, -1    
    for j in range(w):
        if c1 == -1 and blocks[i][j] == 1:
            c1 = j
        elif c1 != -1 and blocks[i][j] == 1:
            c2 = j
            answer += c2 - c1 - 1
            c1 = c2

print(answer)
```
