### 정답 코드
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

        
        
### 오답 코드 - 틀렸습니다.
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


### 오답 코드 - 틀렸습니다.
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


