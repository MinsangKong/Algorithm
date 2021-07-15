import sys
input = sys.stdin.readline

limit = int(1000001**0.5)+1
visited = [1]*1000001
for i in range(2, limit):
    if visited[i] == 0:
        continue
    for j in range(i+i,1000001,i):
        visited[j] = 0

visited[0] = 0
visited[1] = 0

while True:
    num = int(input())
    if num == 0:
        break
    flag = True
    a,b = 0, num
    
    for _ in range(500000):
        if visited[a] and visited[b]:
            flag = True
            break
        a+=1
        b-=1
    
    if flag:
        print("%d = %d + %d" %(num,a,b))
    else:
        print("Goldbach's conjecture is wrong.")