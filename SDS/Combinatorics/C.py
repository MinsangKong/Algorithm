n = int(input())
d = []
for x in range(n):
    a,b = map(int,input().split())
    c = 1
    for i in range(1, a + 1):
        c *= b
        b -= 1
    for j in range(1, a + 1):
        c //= j
    d += [int(c)]
for ans in d:
    print(ans)