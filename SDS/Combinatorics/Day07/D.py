import sys
input = sys.stdin.readline
INF = 1000000001

def getAZ(n,m):
    if n == 0 or m == 0:
        return 1
    if cache[n][m] != -1:
        return cache[n][m]
    cache[n][m] = getAZ(n-1,m)+getAZ(n,m-1)
    if cache[n][m] >= INF:
        cache[n][m] = INF
    return cache[n][m]

n, m, k = map(int, input().split())

cache = [[-1]*(m+1) for _ in range(n+1)]
answer = ""

if getAZ(n,m) < k:
    print(-1)
else:
    for i in range(n+m):
        if n > 0:
            temp = getAZ(n-1,m)
            if temp < k:
                answer+='z'
                k -= temp
                m-=1
            else:
                answer+='a'
                n-=1
        else:
            answer+='z'
            
    print(answer)