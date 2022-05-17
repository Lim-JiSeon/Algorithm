import sys, math
from itertools import combinations

input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]
min_cost = math.inf
answer = []

for cnt in range(1, n+1):
    for pair in combinations(list(range(n)), cnt):
        p,f,s,v,c = 0,0,0,0,0
        for idx in pair:
            p += ingredients[idx][0]
            f += ingredients[idx][1]
            s += ingredients[idx][2]
            v += ingredients[idx][3]
            c += ingredients[idx][4]
        
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if min_cost > c:
                min_cost = c
                answer = list(pair)
            elif min_cost == c:
                answer = sorted((answer,list(pair)))[0]

if min_cost == math.inf:
    print(-1)
else:
    print(min_cost)
    for a in answer:
        print(a+1, end=" ")
