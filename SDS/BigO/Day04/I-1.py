#https://www.acmicpc.net/problem/7453
#백준 합이 0인 네 정수(이분탐색)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

ldict = dict()
rdict = dict()

lnums = []
rnums = []

for i in range(n):
    for j in range(n):
        lnum = nums[i][0]+nums[j][1]
        rnum = nums[i][2]+nums[j][3]
        if lnum in ldict:
            ldict[lnum] += 1
        else:
            ldict[lnum] = 1
            lnums.append(lnum)
        if rnum in rdict:
            rdict[rnum] += 1
        else:
            rdict[rnum] = 1
            rnums.append(rnum)
            
lnums.sort()
rnums.sort()

l, r = 0, len(rnums)-1
cnt = 0
while l <= len(lnums)-1 and r >= 0:
    if lnums[l] +rnums[r] >= 0:
        if lnums[l]+rnums[r] == 0:
            cnt+=ldict[lnums[l]]*rdict[rnums[r]]
        r-=1
    else:
        l+=1
print(cnt)