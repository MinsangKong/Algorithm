import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 1
visited = [0]*(n+1)
result = 0
for i in range(2, n+1):
    if visited[i] == 1:
        continue
    idx = i
    while idx <= n:
        if visited[idx] == 1:
            idx+=i
            continue
        visited[idx] = 1
        if cnt == k:
            result = idx
        idx+=i
        cnt+=1

print(result)