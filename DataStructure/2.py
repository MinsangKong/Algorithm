#https://www.acmicpc.net/problem/10828
#백준 10828번 스택(자료구조)
#import sys
#input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    op = input().rstrip()
    if op[:4] == 'push':
        stack.append(op[5:])
    elif op == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif op == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif op == 'size':
        print(len(stack))
    elif op == 'empty':
        if stack:
            print(0)
        else:
            print(1)