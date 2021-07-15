import sys
input = sys.stdin.readline
from collections import deque

n, k = input().split()
k = int(k)
if int("".join(n)) == 1000000:
    print(1000000)
elif len(n) == 1 or (len(n) == 2 and '0' in n):
    print(-1)
else:
    q = []
    q.append(n)
    for _ in range(k):
        temp = []
        while q:
            num = q.pop()
            num = list(num)
            for i in range(len(n)-1):
                for j in range(i+1,len(n)):
                    num[i],num[j] = num[j], num[i]
                    tem = "".join(num)
                    if tem not in temp:
                        temp.append(tem)
                    num[i],num[j] = num[j], num[i]
        q = temp 
    result = 0
    for num in q:   
        result = max(int(num),result)
    print(result)