#https://www.acmicpc.net/problem/2458
#백준 2458번 키 순서(그래프 이론)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def dfs1(n, i):
    visited1[n] = 1
    for j in info[n][0]:
        if visited1[j] == 0:
            dfs1(j,i)
            result[i].append(j)
            
def dfs2(n, i):
    visited2[n] = 1
    for j in info[n][1]:
        if visited2[j] == 0:
            dfs2(j,i)
            result[i].append(j)
            
    

n, m = map(int, input().split())
info = [[[] for _ in range(2)] for _ in range(n)] #0은 i보다 작은 수 1은 i보다 큰 수
result = [[] for _ in range(n)] 
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    info[b-1][0].append(a-1)
    info[a-1][1].append(b-1)
    
for i in range(n):
    visited1 = [0]*n
    visited2 = [0]*n
    dfs1(i,i)
    dfs2(i,i)
    
for i in range(n):
    if len(result[i]) == n-1:
        cnt+=1
        
print(cnt)