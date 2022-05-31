백준 22352번 항체 인식
======================

### <https://www.acmicpc.net/problem/10713>
<img width="890" alt="image" src="https://user-images.githubusercontent.com/83554018/171173134-61afe466-41d7-4103-8ca3-83cfbbc41891.png">

<hr>

### 코드 설명
+ before와 after을 각각 이중 리스트로 만들어 각 값을 비교하면서 값이 다를 경우에 bfs로 탐색을 진행한다.
+ 탐색할 때 방문한 곳은 before을 after의 값으로 초기화시켜주면서 탐색을 진행하고, 상하좌우 dx,dy를 이용한다.
+ 탐색을 한 뒤에는 check_ans 함수를 통해 항체 가능 여부를 판단한다.

### 소스코드
+ 메모리 : 32508 KB
+ 시간 : 96 ms
```python
from sys import stdin
from collections import deque
input = stdin.readline

def solv():
    for x in range(n):
        for y in range(m):
            if origin[x][y] != transform[x][y]:
                bfs(x,y)
                return check_ans()
    return 'YES'

def bfs(sx,sy):
    global origin
    visited = [[False] * m for _ in range(n)]
    q = deque([(sx,sy)])
    visited[sx][sy] = True
    
    target = origin[sx][sy]
    num = transform[sx][sy]
    while q:
        x,y = q.popleft()
        origin[x][y] = num

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if in_range(nx,ny,visited,target):
                visited[nx][ny] = True
                q.append((nx,ny))

def check_ans():
    for x in range(n):
        for y in range(m):
            if origin[x][y] != transform[x][y]:
                return 'NO'
    return 'YES'

def in_range(x,y,visited,target):
    return 0<=x<n and 0 <=y<m and not visited[x][y] and origin[x][y] == target
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
origin = [list(map(int,input().split())) for _ in range(n)]
transform = [list(map(int,input().split())) for _ in range(n)]

print(solv())
```
