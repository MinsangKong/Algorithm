import sys
input = sys.stdin.readline

def preorder(node):
    preorders.append(node)
    for i in tree[node]:
        if i != '.':
            preorder(i)
    return

def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])
    inorders.append(node)
    if tree[node][1] != '.':
        inorder(tree[node][1])
    return

def postorder(node):
    for i in tree[node]:
        if i != '.':
            postorder(i)
    postorders.append(node)
    return


n = int(input())
tree = dict()

for _ in range(n):
    a,b,c = input().split()
    tree[a] =[]
    tree[a].append(b)
    tree[a].append(c)
    
preorders = []
inorders = []
postorders = []

preorder('A')
inorder('A')
postorder('A')

for i in preorders:
    print(i, end="")
print()
for i in inorders:
    print(i, end="")
print()
for i in postorders:
    print(i, end="")