백준 20444번 색종이와 가위
==========================

### <https://www.acmicpc.net/problem/20444>
<img width="871" alt="image" src="https://user-images.githubusercontent.com/83554018/161481837-a779b1e8-5318-44a9-8df7-17461a8a4c1f.png">

<hr>

### 코드 설명
+ 근의 공식을 이용해서 풀었다. 
+ x와 y를 각각 가로 방향, 세로 방향으로 자른 횟수라면 x + y = n 이고 (x+1)(y+1) = k 이다.
+ 이를 이용해서 x에 대한 이차방정식으로 만든 뒤 근의 공식을 이용해 상수시간 안으로 해결할 수 있도록 만들었다.
+ 루트 안에는 0 이상인 값만 들어가야 하고, 루트를 빠져나왔을 때의 값이 정수여야 하기 때문에 sq을 먼저 검사한 뒤 해를 구해 해가 0 이상인지를 검사했다.

### 소스코드
+ 메모리 : 30864 KB
+ 시간 : 72 ms
```python
import sys
input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
sq = n**2 + 4*(n-k+1)

if sq < 0 or sq != int(sq**0.5)**2:
    print("NO")
else:
    sol1, sol2 = (n + (sq**0.5))/2, (n - (sq**0.5))/2
    if (sol1 >= 0 and sol2 >= 0) and (sol1 == int(sol1) and sol2 == int(sol2)):
        print("YES")

```

### 오답 노트
+ 첫 번째 코드에서는 한번에 계산을 하려고 하다보니 예외처리 되면 안되는 부분이 예외처리되어 no로 출력된 것 같은데 정확한 원인은 아직 발견하지 못했다.
+ 두 번째 코드는 루트 안의 식이 정수로 나올 수 있는지를 확인하는 조건 부분이 문제가 되어 틀린 것으로 출력되는데 루트를 씌워 비교하는 것과 제곱을 해 루트를 빠져나와 비교하는 것 간의 차이를 모르겠다. 


### 오답 코드 - 틀렸습니다.
```python
n, k = tuple(map(int, input().split()))

try:
    x = (n + (n*n + 4*(n-k+1))**0.5)/2
    y = (n - (n*n + 4*(n-k+1))**0.5)/2
    if (x == int(x) and y == int(y)) and (x >= 0 and y >= 0):
        print("YES")
    else:
        print("NO")

except:
    print("NO")
```



### 오답 코드 - 틀렸습니다.
```python
def solve():
    sq = n**2 + 4*(n-k+1)
    if sq < 0:
        print("NO")
        return
    if sq**0.5 != int(sq**0.5):                   # 이 부분 조건 틀림
        print("NO")
        return
    
    sol1, sol2 = (n + (sq**0.5))/2, (n - (sq**0.5))/2
    if sol1 != int(sol1) or sol2 != int(sol2):
        print("NO")
        return
    
    if sol1 >= 0 and sol2 >= 0:
        print("YES")
        return

n, k = tuple(map(int, input().split()))
solve()
```

