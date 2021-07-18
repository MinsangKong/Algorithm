#https://www.acmicpc.net/problem/1202
#백준 1202번 보석도둑 (자료구조)
import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

jewels = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])
pos = 0
checker = []
total = 0

for weight in bags:
    while pos < n and jewels[pos][0] <= weight:
        heapq.heappush(checker, -jewels[pos][1])
        pos+=1
    if checker:
        total+=-heapq.heappop(checker)
    
print(total)