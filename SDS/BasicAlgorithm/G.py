import sys
input = sys.stdin.readline

n = int(input())
num1 = set(list(map(int, input().split())))
m = int(input())
num2 = list(map(int, input().split()))

for i in num2:
    if i in num1:
        print(1)
    else:
        print(0)