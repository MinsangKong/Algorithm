import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

length = int(1e9)
l = 0
r = 1
total = nums[0]

while l < r and r <= n:
    if total >= s:
        length = min(length,r-l)
        total -= nums[l]
        l += 1
    else:
        if r == n:
            break
        total += nums[r]
        r += 1
        
if length == int(1e9):
    print(0)
else:
    print(length)