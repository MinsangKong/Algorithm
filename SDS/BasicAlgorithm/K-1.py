#https://www.acmicpc.net/problem/1339
#백준 1339번 단어 수학(DFS)
#import sys
#input = sys.stdin.readline
from string import ascii_uppercase

def dfs(cnt):
    global result
    if cnt == len(check):
        cost = 0
        for word in words:
            temp = ""
            for i in word:
                temp+=str(book[i])
            cost+=int(temp)
        result = max(cost,result)
        return
    else:
        for j in range(10):
            if visited[j] == 0:
                book[check[cnt]] = j
                visited[j] = 1
                dfs(cnt+1)
                visited[j] = 0
                book[check[cnt]] = 0
        

n = int(input())
words = []
visited = [0]*10
check = set()
book = dict()
result = 0
alpha = list(ascii_uppercase)

for i in alpha:
    book[i] = 0
    
for _ in range(n):
    data = list(input().rstrip())
    words.append(data)
    for i in data:
        check.add(i)
        
check = list(check)
dfs(0)

print(result)
'''
완전 탐색 방식은 시간초과 발생...
'''