#https://www.acmicpc.net/problem/1072
#백준 1072번 게임 1072번 (이분탐색)
x, y = map(int, input().split())
z = int(y*100/x)
W = 1000000000

def search():
    start = 0
    end = W
    while start <= end :
        mid = (start + end) // 2
        changed_z = int((y+mid)*100/(x+mid))
        if changed_z > z:
            end = mid - 1
        else :
            start = mid + 1
    print(end + 1)
if z >= 99:
    print(-1)
else:
    search()