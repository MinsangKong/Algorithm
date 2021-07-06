#https://www.acmicpc.net/problem/1759
#백준 1759번 암호 만들기(DFS)
#import sys
#input = sys.stdin.readline

def dfs(word,idx,vn,cn):
    if len(word) == l:
        if vn >= 1 and cn >= 2 and word not in result:
            result.append(word)
        return
    if idx >= c:
        return
    else:
        if keywords[idx] in vowel:
            dfs(word+keywords[idx],idx+1,vn+1,cn)
        else:
            dfs(word+keywords[idx],idx+1,vn,cn+1)
        dfs(word,idx+1,vn,cn)


l, c = map(int, input().split())
keywords = sorted(list(input().split()))
result = []
vowel = ['a','e','i','o','u']

dfs("",0,0,0)

for i in result:
    print(i)