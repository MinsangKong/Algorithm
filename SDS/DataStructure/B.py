#https://www.acmicpc.net/problem/10845
#백준 10845번 큐(자료구조)
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    oper = input().rstrip()
    if oper[:4] == 'push':
        queue.append(int(oper[5:]))
    elif oper == 'pop':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif oper[0] == 's':
        print(len(queue))
    elif oper[0] == 'e':
        if queue:
            print(0)
        else:
            print(1)
    elif oper[0] == 'f':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif oper[0] == 'b':
        if queue:
            print(queue[-1])
        else:
            print(-1)