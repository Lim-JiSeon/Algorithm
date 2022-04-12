import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(n-1):
    line = list(map(int, input().split()))
    for num in line:
        if heap[0] < num:
            heapq.heappushpop(heap, num)

print(heap[0])



# 백준 : 메모리 초과 
# max heap 구현, heap_sort 이용

n = int(input())
heap = []

for _ in range(n):
    line = input().split()
    for num in line:
        heapq.heappush(heap, (-int(num), int(num)))

heap_sort = []

while len(heap_sort) < n:
    heap_sort.append(heapq.heappop(heap)[1])

print(heap_sort[-1])
