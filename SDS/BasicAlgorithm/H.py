#https://www.acmicpc.net/problem/9663
#백준 9663번 N-Queen(DFS, 백트래킹)
import sys
input = sys.stdin.readline

n = int(input())

check = [0]*15
result = 0

def isTrue(x):
    for i in range(x):
        if check[x] == check[i] or abs(check[x]-check[i]) == x-i:
            return False
    return True

def dfs(num):
    global result
    if num >= n:
        result += 1
    else:
        for i in range(n):
            check[num] = i
            if isTrue(num) :
                dfs(num+1)
                
dfs(0)
print(result)