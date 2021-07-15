import sys
input = sys.stdin.readline

n = list(input().rstrip())

n.sort(reverse = True)
total = sum([int(i) for i in n])

if n[-1] == '0' and total % 3 == 0:
    
    print(int("".join(n)))
else:
    print(-1)