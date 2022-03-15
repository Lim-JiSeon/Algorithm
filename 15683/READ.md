백준 15683번 감시
==================

### <https://www.acmicpc.net/problem/15683>
<img width="882" alt="image" src="https://user-images.githubusercontent.com/83554018/158316003-0f85ada1-0b85-4ac7-bcd1-8d7b51b20e4e.png">

<hr>

### 코드 설명
+ in_range() 함수는 x와 y가 board 범위 밖인지 아닌지를 확인하는 함수로 범위 밖이면 false를 범위 안이면 true를 리턴한다.
+ direction_check() 함수는 방향을 확인해 direction이란 리스트에 넣어주는 함수로 cctv 종류에 따라 현재방향을 기준으로 방향을 넣어준다. <br> 예) cctv가 2번이면 현재방향을 기준으로 현재방향과 정반대 방향 총 2방향을 감시할 수 있으므로, direction에 2방향의 값을 넣어준다.
+ bfs() 함수는 direction을 기준으로 벽을 만나기 전까지 그 방향의 board 끝까지 확인하면서 visited를 1로 초기화해준다.
+ cnt, 즉 cctv의 개수를 1씩 증가시키면서 solution을 돌린 뒤 cnt가 모든 cctv의 개수가 되면 사각지대를 세어준 뒤 기존의 값과 비교해 더 작은 값을 answer에 초기화해준다.
+ back_visited() 함수는 기존의 visited를 초기화해준 것을 다시 0으로 초기화해줌으로써 원상태로 돌려준다.  

### 소스코드
+ 메모리 : 32564 KB
+ 시간 : 1056 ms
```python
import sys
from collections import deque

input = sys.stdin.readline

def in_range(x,y):
	return 0 <= x < n and 0 <= y < m

def direction_check(x,y,k):
	direction = []
	if board[x][y] == 1: 
		direction.append(k)
	elif board[x][y] == 2:
		direction.append(k)
		direction.append((k + 2) % 4)
	elif board[x][y] == 3:
		direction.append(k)
		direction.append((k - 1) % 4)
	elif board[x][y] == 4:
		direction.append(k)
		direction.append((k - 1) % 4)
		direction.append((k + 2) % 4)
	elif board[x][y] == 5:
		direction.append(k)
		direction.append((k - 1) % 4)
		direction.append((k + 1) % 4)
		direction.append((k + 2) % 4)

	return direction

def bfs(x,y,k):
	global visited
	direction = direction_check(x,y,k)

	q = deque()
	for d in direction: 
		nx, ny = x + dx[d], y + dy[d]
		while in_range(nx,ny): 
			if not visited[nx][ny] and board[nx][ny] != 6: 
				visited[nx][ny] = 1 
				q.append((nx, ny))
			elif board[nx][ny] == 6: break 
			nx += dx[d]
			ny += dy[d]

	return q


def back_visited(q):
	global visited
	while q:
		qx, qy = q.popleft()
		if not board[qx][qy]:
			visited[qx][qy] = 0

def solution(cnt):
	global visited, answer
	if cnt == cctv_n:
		tmp = 0
		for i in range(n):
			for j in range(m):
				if not board[i][j] and not visited[i][j]:
					tmp += 1
		return tmp

	x, y = cctv[cnt]

	for k in range(4):
		queue = bfs(x,y,k)
		answer = min(answer, solution(cnt + 1))
		back_visited(queue)
		if board[x][y] == 5: break
	return answer

n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = []
cctv_n = 0 
answer = 0 
visited = [[0] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
	for j in range(m):
		if board[i][j] and board[i][j] != 6:
			cctv.append((i, j))
			visited[i][j] = True
			cctv_n += 1
		if not board[i][j]:
			answer += 1

solution(0)
print(answer)

```
