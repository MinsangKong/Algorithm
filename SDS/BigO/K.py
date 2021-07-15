#https://www.acmicpc.net/problem/11003
#백준 11003번 최솟값 찾기(자료구조)
#import sys
#input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
nums = list(map(int, input().split()))

q = deque()
result = []

for i in range(n):
    num = nums[i]
    while q and q[-1] > num:
        q.pop()
    q.append(num)
    if i >= l and q[0] == nums[i-l]:
        q.popleft()
    print(q[0], end = ' ')
            