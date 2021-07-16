#https://www.acmicpc.net/problem/1103
#백준 1103번 게임(DP,DFS)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if dp[x][y] != 1:
        return dp[x][y]
    visited[x][y] = 1
    for a,b in direction:
        num = int(board[x][y])
        nx = x+(a*num)
        ny = y+(b*num)
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'H':
            if visited[nx][ny]:
                print(-1)
                sys.exit()
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    visited[x][y] = 0
    return dp[x][y]
    
n, m = map(int, input().split())
direction = [(1,0),(-1,0),(0,1),(0,-1)]
board = [list(input().rstrip()) for _ in range(n)]
dp = [[1]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

print(dfs(0,0))