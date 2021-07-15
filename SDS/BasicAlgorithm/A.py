#https://www.acmicpc.net/problem/3425
#백준 3425번 고스택(구현)
import sys
#input = sys.stdin.readline

def command(oper,num):
    stack = []
    stack.append(num)
    for op in oper:
        if op[0] == 'N':
            if op[4] == '-':
                x = int(op[5:])*-1
            else:
                x = int(op[4:])
            stack.append(x)
        elif op[0] == 'P':
            if stack:
                stack.pop()
            else:
                print("ERROR")
                return
        elif op[0] == 'I':
            if stack:
                inv = stack.pop()
                stack.append(-inv)
            else:
                print("ERROR")
                return
        elif op == 'DUP':
            if stack:
                d = stack[-1]
                stack.append(d)
            else:
                print("ERROR")
                return
        elif op == 'SWP':
            if len(stack) >= 2:
                stack[-1],stack[-2] = stack[-2],stack[-1]
            else:
                print("ERROR")
                return
        elif op[0] == 'A':
            if len(stack) >= 2:
                a = stack.pop()
                stack[-1]+=a
                if abs(stack[-1]) > 10**9:
                    print("ERROR")
                    return
            else:
                print("ERROR")
                return
        elif op == 'SUB':
            if len(stack) >= 2:
                s = stack.pop()
                stack[-1] -= s
                if abs(stack[-1]) > 10**9:
                    print("ERROR")
                    return
            else:
                print("ERROR")
                return
        elif op == 'MUL':
            if len(stack) >= 2:
                m = stack.pop()
                stack[-1]*= m
                if abs(stack[-1]) > 10**9:
                    print("ERROR")
                    return
            else:
                print("ERROR")
                return
        elif op == 'DIV':
            if len(stack) >= 2:
                if stack[-1] == 0:
                    print("ERROR")
                    return
                else:
                    d = stack.pop()
                    cnt = 0
                    if d < 0 :
                        cnt +=1
                        d = abs(d)
                    if stack[-1] < 0:
                        cnt += 1
                        stack[-1] *= -1
                    d = stack[-1]//d
                    if cnt%2 == 0:
                        stack[-1] = d
                    else:
                        stack[-1] = -d
                    if abs(stack[-1]) > 10**9:
                        print("ERROR")
                        return
            else:
                print("ERROR")
                return
        elif op == 'MOD':
            if len(stack) >= 2:
                if stack[-1] == 0:
                    print("ERROR")
                    return
                else:
                    m = stack.pop()
                    cnt = 0
                    if stack[-1] < 0:
                        cnt += 1
                        stack[-1] *= -1
                    m = stack[-1] % abs(m)
                    if cnt != 1:
                        stack[-1] = m
                    else:
                        stack[-1] = -m
                    if abs(stack[-1]) > 10**9:
                        print("ERROR")
                        return
            else:
                print("ERROR")
                return

    if len(stack) == 1:
        print(stack[0])
    else:
        print("ERROR")
    return

while True:
    oper = []
    while True:
        op = input().rstrip()
        if op[0] == 'Q':
            sys.exit()
        if op[0] == 'E':
            break
        oper.append(op)
    n = int(input())
    for i in range(n):
        num = input()
        if num[0] == '-':
            num = int(num[1:])*-1
        else:
            num = int(num)
        command(oper, num)
    print()
    input().rstrip()