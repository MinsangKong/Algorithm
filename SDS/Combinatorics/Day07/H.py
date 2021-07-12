import sys
input = sys.stdin.readline

w, h = map(int, input().split())
dp = [[[[0]*2 for _ in range(2)] for _ in range(h+1)] for _ in range(w+1)]

for i in range(2,w+1):
    dp[i][1][0][0] = 1
    
for i in range(2,h+1):
    dp[1][i][0][1] = 1
    
for i in range(2,w+1):
    for j in range(2,h+1):
        dp[i][j][0][0] = (dp[i - 1][j][0][0] + dp[i - 1][j][1][0])%100000
        dp[i][j][0][1] = (dp[i][j - 1][0][1] + dp[i][j - 1][1][1])%100000
        dp[i][j][1][0] = (dp[i - 1][j][0][1])%100000
        dp[i][j][1][1] = (dp[i][j - 1][0][0])%100000
print((dp[w][h][0][0] + dp[w][h][0][1] + dp[w][h][1][0] + dp[w][h][1][1])%100000)