def solution(n):                      # n을 1씩 줄이고, answer을 계산하는 함수 (= 4분할하면서 이제까지 지나왔던 경로들을 모두 더하는 함수)
    global answer
    if n == 1:                        # answer에 초기값을 주었기 때문에 n이 1이면 빠져나올 것
        return
    
    size = (2**(n-1))**2              # 4분할했을 때 그 4분할한 것들 중 하나의 크기
    quadrant = find_quadrant(n)       # 4분할해서 (r,c)의 좌표가 어떤 사분면에 속하는지 알아내서 quadrant에 저장 -> 겪어온 경로를 더하는 과정애서 size를 몇번 더해줘야 하는지를 알아내기 위함 
    answer += size*quadrant           # answer에 더해주기
    
    solution(n-1)                     # n을 1씩 줄여줌 -> n이 1이 될때까지 계속 4분할한다는 의미
    
   
    
def find_quadrant(n):                 # r,c 좌표가 무슨 사분면에 속하는지 찾는 함수
    global r, c
    k = 2**(n-1)                      # 4분할했을 때 사분면을 나누는 기준
    if r < k and c < k:               # r,c가 모두 k보다 작은 쪽은 r과c를 재초기화해줄 필요가 없음
        return 0
    elif r < k and c >= k:            # r은 k보다 작기 때문에 그대로, c는 k이상이므로 분할할 때 좌표범위가 작아질 것을 생각해 c를 재초기화해줌
        c -= k
        return 1
    elif r >= k and c < k:            # c는 k보다 작기 때문에 그대로, r은 k이상이므로 분할할 때 좌표범위가 작아질 것을 생각해 r을 재초기화해줌
        r -= k  
        return 2
    else:                             # r,c 모두 k 이상이기 때문에 재초기화해줌
        r -= k
        c -= k
        return 3
    
    
n,r,c = tuple(map(int, input().split()))
matrix = [[0,1],[2,3]]                      # 초기값 설정 (= n이 1일때)
answer = matrix[r%2][c%2]                   # 초기값 설정 (n이 1일때의 r과 c의 값)

solution(n)
print(answer)
