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
