#https://www.acmicpc.net/problem/1339
#백준 1339번 단어 수학(그리디)
#import sys
#input = sys.stdin.readline
n = int(input())

words = []
answer = 0
book = dict()
for _ in range(n):
    word = list(input().rstrip())
    words.append(word)
    length = len(word)-1
    for i in range(len(word)):
        if word[i] in book:
            book[word[i]] += 10**(length)
        else:
            book[word[i]] = 10**(length)
        length -=1
book = dict(sorted(book.items(), key = lambda x : x[1], reverse = True))

result = 0
pivot = 9
for word in book:
    result+=book[word]*pivot
    pivot-=1
print(result)