#https://www.acmicpc.net/problem/7453
#백준 합이 0인 네 정수(이분탐색)
#import sys
#input = sys.stdin.readline

n = int(input())
alist, blist, clist, dlist = [], [], [], []

for _ in range(n):
    a,b,c,d = map(int, input().split())
    alist.append(a)
    blist.append(b)
    clist.append(c)
    dlist.append(d)

ldict = dict()

for a in alist: 
    for b in blist: 
        if a+b not in ldict: 
            ldict[a+b] = 1 
        else: 
            ldict[a+b] += 1 

cnt = 0
for c in clist: 
    for d in dlist: 
        if -(c+d) in ldict:
            cnt += ldict[-(c+d)]
print(cnt)
'''
dict를 사용하는 것보다 정렬한 뒤 중분한 갯수를 세고 이분탐색하는 방식이 더 빨랐다.
'''