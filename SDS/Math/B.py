import sys
input = sys.stdin.readline

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)
    
n = int(input())
nums = list(map(int, input().split()))
lgcd = [0]*(n+2)
rgcd = [0]*(n+2)

for i in range(1,n+1):
    lgcd[i] = gcd(lgcd[i-1],nums[i-1])
for i in range(n,-1,-1):
    rgcd[i] = gcd(rgcd[i+1],nums[i-1])
    
result = 0
idx = 0
for i in range(1,n+1):
    curgcd = gcd(lgcd[i-1],rgcd[i+1])
    if nums[i-1] % curgcd == 0:
        continue
    if result < curgcd:
        result = curgcd
        idx = nums[i-1]
        
if result == 0:
    print(-1)
else:
    print(result, idx)