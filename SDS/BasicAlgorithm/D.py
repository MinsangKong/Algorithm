#https://www.acmicpc.net/problem/1713
#백준 1713번 후보 추천하기(그리디, 구현)
import sys
input = sys.stdin.readline
def check_graph():
    for i in range(n):
        if graph[i] == 0:
            return i
    pos = 0
    check_when = 1000
    check_like = 1000
    
    for i in range(n):
        cur = graph[i]
        temp_like = students[cur][0]
        temp_when = students[cur][2]
        if check_like > temp_like:
            check_like = temp_like
            check_when = temp_when
            pos = i
        elif check_like == temp_like and temp_when < check_when:
            check_like = temp_like
            check_when = temp_when
            pos = i
    return pos
    
n = int(input())
total = int(input())
orders = list(map(int, input().split()))
students = [[-1]*3 for _ in range(101)] #표, 위치, 올라간 순서
pos = 0
graph = [0]*n


for i in range(total):
    order = orders[i]
    if students[order][1] != -1:
        students[order][0] += 1
    else:
        pos = check_graph()
        delete_cand = graph[pos]
        if delete_cand != 0:
            students[delete_cand][1] = -1
            students[delete_cand][0] = 0
            
        students[order][1] = pos
        students[order][0] = 1
        students[order][2] = i
        graph[pos] = order
        
for i in range(1,101):
    if students[i][1] != -1:
        print(i, end=" ")