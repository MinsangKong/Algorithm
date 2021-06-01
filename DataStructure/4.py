#https://www.acmicpc.net/problem/2164
#백준 2614번 카드2(자료구조)
#import sys
#input = sys.stdin.readline
from collections import deque

n = int(input())
cards = deque([i+1 for i in range(n)])

while True:
    if len(cards) == 1:
        print(cards[0])
        break
        
    cards.popleft()
    num = cards.popleft()
    cards.append(num)