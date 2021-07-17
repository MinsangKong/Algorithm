#https://www.acmicpc.net/problem/2805
#백준 2805번 나무 자르기(이분탐색)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
start = 0
end = trees[-1]
result = 0
while start <= end:
    mid = (start+end)//2
    sub = 0
    for i in trees:
        if i > mid:
            sub+=i-mid
    if sub >= m:
        result = mid
        start = mid + 1    
    else:
        end = mid - 1
            
print(result)