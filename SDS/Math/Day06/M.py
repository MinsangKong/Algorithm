#https://www.acmicpc.net/problem/2904
#백준 2904번 수학은 너무 쉬워(정수론)
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
primes = []
line = max(nums)
limit = int(line**0.5)+1
visited = [0]*(line+1)

for i in range(2,limit):
    if visited[i] == 1:
        continue
    for j in range(i+i,line+1,i):
        visited[j] = 1
for i in range(2, line+1):
    if not visited[i]:
        primes.append(i)
        
count = [[0]*len(primes) for _ in range(n)]
total = [0]*len(primes)
gcdCount = [0]*len(primes)

for i in range(n):
    num = nums[i]
    for j in range(len(primes)):
        if num % primes[j] == 0:
            while num % primes[j] == 0:
                count[i][j] +=1
                total[j]+=1
                num = num//primes[j]
                
for i in range(len(primes)):
    gcdCount[i] = total[i]//n
    
result1, result2 = 1, 0

for i in range(len(primes)):
    for j in range(gcdCount[i]):
        result1 *= primes[i]
    
    for j in range(n):
        if count[j][i] < gcdCount[i]:
            result2 += gcdCount[i] - count[j][i]
            
print(result1, result2)