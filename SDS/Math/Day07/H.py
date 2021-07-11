import sys
input = sys.stdin.readline

p, k = map(int, input().split())

visited= [1]*(k+1)
limit = int(k**0.5)+1
visited[0] = 0
visited[1] = 0

for i in range(2,limit):
    if visited[i] == 0:
        continue
    for j in range(i+i,k+1,i):
        visited[j] = 0
        
flag= True
result = 0
for i in range(2,k):
    if visited[i] and p%i == 0:
        result = i
        flag = False
        break
        
if flag:
    print("GOOD")
else:
    print("BAD %d" %result)