import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []

for _ in range(n):
    oper = int(input())
    if oper == 0:
        if arr:
            num = heapq.heappop(arr)
            print(-num)
        else:
            print(0)
    else:
        heapq.heappush(arr,-oper)