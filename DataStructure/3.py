#https://www.acmicpc.net/problem/9012
#백준 9012번 괄호(자료구조)
#import sys
#input = sys.stdin.readline

n = int(input())

for _ in range(n):
    vps = input().rstrip()
    
    check = 0
    flag = True
    
    for i in range(len(vps)):
        if vps[i] == '(':
            check+=1
        elif vps[i] == ')':
            if check == 0:
                flag = False
                break
            check-=1
            
    if not flag or check != 0:
        print("NO")
    else:
        print("YES")