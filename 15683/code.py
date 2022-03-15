import sys
from collections import deque

input = sys.stdin.readline

def in_range(x,y):                            # x,y 가 range 안에 속하는지 아닌지 확인하는 함수
	return 0 <= x < n and 0 <= y < m            # x 또는 y가 범위 밖이면 False를 리턴, 둘다 범위 안이면 True를 리턴

def direction_check(x,y,k):                   # cctv 종류에 따른 방향을 direction 리스트에 넣어준 뒤 리턴해주는 함수
	direction = []
	if board[x][y] == 1:                        # 1번 cctv 한 방향만 감시 
		direction.append(k)                       # 현재 방향만 direction에 넣어주면 됨
	elif board[x][y] == 2:                      # 2번 cctv 두 방향 감시 
		direction.append(k)                       # 현재 방향과 현재 방향의 정 반대 방향을 direction에 넣어주면 됨
		direction.append((k + 2) % 4)             # 방향을 0,1,2,3 이라 했을 때 0의 정반대는 2, 1의 정반대는 3 2의 정반대는 0 이런식으로 계산하면 원래방향에 2를 더한 뒤 4로 나눈 나머지가 정반대 방향임
	elif board[x][y] == 3:                      # 3번 cctv 두 방향 감시
		direction.append(k)                       # 현재 방향과 현재 방향을 기준으로 왼쪽 90도 방향을 direction에 넣어주면 됨
		direction.append((k - 1) % 4)             # 위에서와 마찬가지로 0일때 3, 1일때 0, 3일때 2인 것을 생각하면 원래 방향에 -1을 한 뒤 4로 나눈 나머지를 넣어주면 됨(보충설명 )
	elif board[x][y] == 4:                      # 4번 cctv 세 방향을 감시
		direction.append(k)                       # 현재 방향과 현재 방향을 기준으로 정반대와 왼쪽 90도 방향을 direction에 넣어주면 됨
		direction.append((k - 1) % 4)             # 아까와 같은 방식으로 계산해서 넣어주기
		direction.append((k + 2) % 4)
	elif board[x][y] == 5:                      # 5번 cctv 네 방향을 감시
		direction.append(k)                       # 세 방향은 위에서 했던 대로 같게 해서 direction에 넣어주기
		direction.append((k - 1) % 4)
		direction.append((k + 1) % 4)             # 현재 방향을 기준으로 오른쪽 90도 방향이므로 0이면 1, 1이면 2, 2면 3, 3이면 0 이기 때문에 1을 더해준 뒤 4로 나눈 나머지를 넣어주면 됨
		direction.append((k + 2) % 4)

	return direction                            # cctv 방향이 담긴 리스트 리턴 

def bfs(x,y,k):                                               # cctv의 방향대로 방문하면서 visited을 1로 초기화 시켜주는 함수
	global visited
	direction = direction_check(x,y,k)                          # 위의 방향을 넣어주는 함수를 호출해 cctv 방향이 담긴 리스트를 받음 -> direction

	q = deque()
	for d in direction:                                         # cctv 방향을 기준으로 탐색
		nx, ny = x + dx[d], y + dy[d]
		while in_range(nx,ny):                                    # 범위 밖으로 나갈때까지 끝까지 방문
			if not visited[nx][ny] and board[nx][ny] != 6:          # 벽이 아니고 방문하지 않았다면
				visited[nx][ny] = 1                                   # 방문했다는 표시로 visited을 1로 초기화
				q.append((nx, ny))                                    # 방문 좌표를 q에 넣어줌
			elif board[nx][ny] == 6: break                          # 벽이라면 빠져나오기 -> 더는 방문하지 못하기 때문
			nx += dx[d]                                             
			ny += dy[d]

	return q


def back_visited(q):                                          # visited를 원상복귀 시켜주는 함수
	global visited
	while q:
		qx, qy = q.popleft()
		if not board[qx][qy]:                                     # 방문했던 곳들을 다시 0으로 초기화
			visited[qx][qy] = 0

def solution(cnt):
	global visited, answer
	if cnt == cctv_n:                                           # 모든 cctv 확인 했으면 사각지대 개수 세주기
		tmp = 0                                                   # 사각지대의 개수를 임의로 저장할 변수
		for i in range(n):
			for j in range(m):
				if not board[i][j] and not visited[i][j]:             # board의 값이 0 이고 visited의 값이 0이면 사각지대란 의미 -> cctv가 감시했다면 visited의 값이 1이 됨
					tmp += 1
		return tmp                                                # 사각지대 개수 리턴              
 
	x, y = cctv[cnt]                                            # cctv 좌표를 x, y에 저장

	for k in range(4):                                          # cctv 의 4방향 확인
		queue = bfs(x,y,k)                                        # cctv를 통해 visited에 감시했다는 표시로 1로 초기화해주기 위함
		answer = min(answer, solution(cnt + 1))                   # 위의 과정을 거친 뒤 사각지대를 세어 기존의 answer과 비교해 더 작은 값을 answer에 넣어줌
		back_visited(queue)                                       # 다른 방향들도 확인을 해주기 위해 visited을 원상복귀 시켜줌 -> 방문했던 곳을 0으로 돌려줌
		if board[x][y] == 5: break                                # 5번 cctv는 4방향이기 때문에 회전시켜줄 필요 없음  
	return answer

n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = []                                                       # cctv 좌표 저장할 리스트
cctv_n = 0                                                      # board 안의 모든 cctv 개수 
answer = 0                                                      # 사각지대 최소값 저장 
visited = [[0] * m for _ in range(n)]                           # 방문 여부 저장 -> 방문하지 않았으면 0, 방문했으면 1

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]                           # 우 하 좌 상

for i in range(n):
	for j in range(m):
		if board[i][j] and board[i][j] != 6:                        # board의 값이 0이 아니고, 6이 아닐때 -> 즉 cctv가 있다는 의미
			cctv.append((i, j))                                       # cctv 좌표 넣고 방문했다는 표시로 1로 초기화
			visited[i][j] = 1
			cctv_n += 1                                               # 모든 cctv의 개수를 세기 위해 1씩 더해줌
		if not board[i][j]:                                         # 최대 사각지대를 answer의 초기값으로 넣어줌
			answer += 1                                               # board의 값이 0이란 의미는 사각지대란 의미

solution(0)                                                     # cnt를 0으로 초기값 주고 시작
print(answer)
