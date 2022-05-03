백준 11048번 이동하기
=====================

### <https://www.acmicpc.net/problem/11048>
<img width="876" alt="image" src="https://user-images.githubusercontent.com/83554018/166423022-34801af6-e92c-453c-b9a8-d4a8387f91b0.png">

<hr>

### 코드 설명
+ 이동하면서 사탕의 개수를 누적해서 더한 합을 저장할 공간을 하나 만들어준다. -> dp
+ 이중 for문을 통해 이동하면서 이동할 수 있는 방향키 3곳의 방향과 비교해 가장 큰 값이 있는 곳을 선정한 뒤 새로운 사탕의 개수를 더해준다.
+ 위에서 방향키 3곳은 dp안에 있는 누적 사탕개수를 비교해 최대값을 따져야 한다.

### 소스코드
+ 메모리 : 38528 KB
+ 시간 : 992 ms
```python
import sys
input = sys.stdin.readline

n,m = tuple(map(int, input().split()))
maze = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(m+1)]*(n+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i-1][j-1]

print(dp[n][m])
```
