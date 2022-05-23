import sys
input = sys.stdin.readline

n,m = tuple(map(int, input().split()))
maze = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(m+1)]*(n+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i-1][j-1]

print(dp[n][m])