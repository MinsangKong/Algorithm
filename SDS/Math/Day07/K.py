import sys

data = sys.stdin.read()
nums = data.split('\n')

for num in nums:
    if num != '':
        num = int(num)
        idx = 1
        s = 1
        if num == 1:
            print(1)
        else:
            while s!= 0:
                s = (s*10+1)%num
                idx+=1
            print(idx)