import sys
input = sys.stdin.readline
import heapq

n = int(input())
nums = []
maxheapq = []
minheapq = []

for i in range(n):
    num = int(input())
    
    if len(maxheapq) == len(minheapq):
        heapq.heappush(maxheapq, -num)
    else:
        heapq.heappush(minheapq, num)
        
    if maxheapq and minheapq and -maxheapq[0] > minheapq[0]:
        maxnum = heapq.heappop(maxheapq)
        minnum = heapq.heappop(minheapq)
        heapq.heappush(minheapq, -maxnum)
        heapq.heappush(maxheapq, -minnum)
        
    print(-maxheapq[0])