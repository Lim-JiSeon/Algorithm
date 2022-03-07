import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
result = [-1]*n

stack = []
for i in range(n):
    while stack and stack[-1][0] < lst[i]:
        value, index = stack.pop()
        result[index] = lst[i]
    stack.append([lst[i],i])

for r in result:
    print(r, end=" ")
