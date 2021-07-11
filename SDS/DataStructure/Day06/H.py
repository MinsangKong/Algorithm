import sys

book = dict()
length = 0

data = sys.stdin.read()
trees = data.split('\n')

for t in trees:
    if t != '':
        length +=1
        if t in book:
            book[t] += 1
        else:
            book[t] = 1
        
for key, value in sorted(book.items()):
    print("{} {:.4f}".format(key,(value/length)*100))