#https://www.acmicpc.net/problem/2580
#백준 2580번 스도쿠(백트래킹,DFS,완전탐색)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit

def dfs(depth):
    if depth == len(check):
        if isRight():
            for i in board:
                print(*i)
            sys.exit()
        return
    else:
        x,y = check[depth][0],check[depth][1]
        ynums = set()
        for i in range(9):
            ynums.add(board[i][y])
        three = set()
        dx = x//3
        dy = y//3
        for i in range(dx*3, dx*3+3):
            for j in range(dy*3, dy*3+3):
                three.add(board[i][j])
        possible = nums- set(board[x])-ynums-three
        for i in possible:
            board[x][y] = i
            dfs(depth+1)
            board[x][y] = 0
    
def isRight():
    for i in range(9):
        total = 0
        if sum(board[i]) != 45:
            return False
        for j in range(9):
            total += board[j][i]
        if total != 45:
            return False
        
    for k in range(0,9,3):
        total = 0
        for i in range(k,k+3):
            for j in range(k,k+3):
                total += board[i][j]
        if total != 45:
            return False
    return True

board = []
check = []
nums = {1,2,3,4,5,6,7,8,9}
for i in range(9):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(9):
        if data[j] == 0:
            check.append([i,j])

dfs(0)