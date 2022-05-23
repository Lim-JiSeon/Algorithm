import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
p = list(map(int, input().split()))
cost = [list(map(int, input().split())) for _ in range(n-1)]
freq = [0 for _ in range(n)]
min_cost = 0

for idx in range(m-1):
    s, e = min(p[idx], p[idx+1]), max(p[idx], p[idx+1])
    freq[s-1] += 1
    freq[e-1] -= 1

for idx in range(1,n):
    freq[idx] = freq[idx-1] + freq[idx]

for idx in range(n-1):
    if freq[idx] > 0:
        min_cost += min(freq[idx]*cost[idx][0], freq[idx]*cost[idx][1] + cost[idx][2])

print(min_cost)
