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
