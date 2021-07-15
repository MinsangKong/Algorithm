import sys
input = sys.stdin.readline
import heapq

k, n = map(int, input().split())

primes = list(map(int, input().split()))
totals = []

for prime in primes:
    heapq.heappush(totals, prime)
    
cnt = 0
result = 0
while True:
    num = heapq.heappop(totals)
    for prime in primes:
        heapq.heappush(totals, num*prime)
        if num % prime == 0:
            break
    cnt += 1
    if cnt == n:
        result= num
        break
print(result)