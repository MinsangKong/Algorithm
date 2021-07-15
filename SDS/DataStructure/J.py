import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            min_num = heapq.heappop(heap)
            print(min_num)
        else:
            print(0)
    else:
        heapq.heappush(heap,num)