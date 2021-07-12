import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = 1

for i in range(n,n-k,-1):
    result *= i 
    
for j in range(2,k+1):
    result = result // j
    
print(result)