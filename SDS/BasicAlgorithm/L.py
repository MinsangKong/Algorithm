#https://www.acmicpc.net/problem/15686
#백준 15686번 치킨 배달(구현, 순열)
import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())

nums = list(map(int, input().split()))
result = set()
for i in permutations(nums, m):
    flag = True
    for j in range(1,m):
        if i[j] < i[j-1]:
            flag = False
            break
    if flag:
        result.add(i)
    
for i in sorted(result):
    print(*i)