#https://www.acmicpc.net/problem/1062
#백준 1062번 가르침(그리디,조합)
import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())
base = ['a','n','t','i','c']
words = []
for _ in range(n):
    data = input().rstrip()
    words.append(set(list(data[4:-4])))

if k < 5:
    print(0)
else:
    k -=5
    check = set()
    for word in words:
        for j in word:
            if j not in base:
                check.add(j)
    result = 0
    if len(check) <= k:
        result = n
    elif len(check) == 1:
            point = 0
            for word in words:
                if not word:
                    point += 1
            result = point
    else:
        for com in combinations(check, k):
            point = 0
            for word in words:
                flag = True
                for alp in word:
                    if alp not in base and alp not in com:
                        flag = False
                        break
                if flag:
                    point +=1
            result = max(result,point)
    print(result)