백준 1074번 Z
===============

### <https://www.acmicpc.net/problem/1074>
<img width="889" alt="image" src="https://user-images.githubusercontent.com/83554018/158282519-cfdf9988-cf74-44d2-8d7e-0f0280f18d8a.png">

<hr>

### 코드 설명
+ find_quadrant 함수는 4분할했을 때 r,c의 좌표가 몇 사분면에 있는지 찾는 함수이다. 
+ solution 함수는 n의 크기를 1씩 줄이고, answer에 값을 더해주는 함수로 n이 1이 될때까지 계속 줄여주면서 4분할한다.
+ answer의 초기값을 이미 설정해줬기 때문에 n이 1이 될때까지 반복한다. (초기값은 n이 1일때 설정해주는 것과 같다.)

### 소스코드
+ 메모리 : 30864 KB
+ 시간 : 68 ms
```python
def solution(n):
    global answer
    if n == 1:
        return
    
    size = (2**(n-1))**2
    quadrant = find_quadrant(n)
    answer += size*quadrant
    
    solution(n-1)
    
   
    
def find_quadrant(n):
    global r, c
    k = 2**(n-1)
    if r < k and c < k:
        return 0
    elif r < k and c >= k:
        c -= k
        return 1
    elif r >= k and c < k:
        r -= k
        return 2
    else:
        r -= k
        c -= k
        return 3
    
    
n,r,c = tuple(map(int, input().split()))
matrix = [[0,1],[2,3]]
answer = matrix[r%2][c%2]

solution(n)
print(answer)

```

### 오답 노트
+ 메모리 초과 - 굳이 matrix를 만들어 초기화시켜줄 필요가 없었다. 메모리 제한용량이 크지 않기 때문에 효율적으로 짜야 한다.
+ 틀렸습니다 - find_quadrant 함수를 구현하는 과정에서 n을 1씩 줄여나가는 것이기 때문에 기준점을 재초기화하기보다는 r과 c를 초기화시켜주는 편이 직관적이고 쉽다.


### 오답 코드 - 메모리초과
```python
def fill_matrix(n):
    if n == 0:
        return
    
    fill_matrix(n-1)
    
    for i in range(2**n):
        for j in range(2**n):
            size = (2**(n-1))**2
            quadrant = find_quadrant(n,i,j)
            matrix[i][j] = matrix[i%2**(n-1)][j%2**(n-1)] + size*quadrant
    return

def find_quadrant(n,r,c):
    k = 2**(n-1)
    if r < k and c < k:
        return 0
    elif r < k and c >= k:
        return 1
    elif r >= k and c < k:
        return 2
    else:
        return 3

n,r,c = tuple(map(int, input().split()))
matrix = [[0]*(2**(n-1)) for _ in range(2**(n-1))]

fill_matrix(n-1)

if n == 1:
    print(find_quadrant(n,r,c))
else:
    size = (2**(n-1))**2
    quadrant = find_quadrant(n,r,c)
    answer = matrix[r%(2**(n-1))][c%(2**(n-1))] + size*quadrant
    print(answer)
```



### 오답 코드 - 틀렸습니다.
```python
def solution(n):
    global answer
    if n == 1:
        return
    
    size = (2**(n-1))**2
    quadrant = find_quadrant(n,r,c)
    answer += size*quadrant
    
    solution(n-1)
    
   
    
def find_quadrant(n,r,c):
    global x, y
    k = 2**(n-1)
    if r < k+x and c < k+y:
        x,y = 0,0
        return 0
    elif r < k+x and c >= k+y:
        x,y = 0,k
        return 1
    elif r >= k+x and c < k+y:
        x,y = k,0
        return 2
    else:
        x,y = k,k
        return 3
    
    
n,r,c = tuple(map(int, input().split()))
matrix = [[0,1],[2,3]]
answer = matrix[r%2][c%2]
x,y = 0,0

if n == 1:
    print(matrix[r][c])
else:
    solution(n)
    print(answer)
```

