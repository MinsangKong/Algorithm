#https://www.acmicpc.net/problem/2504
#백준 2504번 괄호의 값(문자열)
import sys
input = sys.stdin.readline
s = input().rstrip()
stack = []
result = 0

for i in s:
    if i == ')':
        last = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if last == 0:
                    stack.append(2)
                else:
                    stack.append(2 * last)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                last+=int(top)

    elif i == ']':
        last = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if last == 0:
                    stack.append(3)
                else:
                    stack.append(3 * last)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                last += int(top)
 
    else:
        stack.append(i)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
print(sum(stack))