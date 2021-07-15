#https://www.acmicpc.net/problem/11438
#백준 11438번 LCA2(LCA)
import sys
input = sys.stdin.readline
from math import log2
from collections import deque


        
def set_parent():
    q=deque()
    q.append(1)
    visited = [1]*(n+1)
    while q:
        p=q.popleft()
        visited[p]=0
        for node in graph[p]:
            if visited[node]:
                q.append(node)
                parent[node][0]=p
                depth[node]=depth[p]+1#깊이도 같이 저장해준다.

    for i in range(1,logN):
        for j in range(1,n+1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i-1]][i-1]
            
def lca(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    
    for i in range(logN-1,-1,-1):
        if depth[b]-depth[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a
    
    #올라가면서 공통 조상 찾기
    for i in range(logN-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

n = int(input())
logN = int(log2(n)+1)
parent = [[0]*logN for _ in range(n+1)]
depth = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
set_parent()

m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))