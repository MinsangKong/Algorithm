import sys
input = sys.stdin.readline
def gcd(m, n):
    if n > m:
        return gcd(n,m)
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)

a,b = map(int, input().split())
c,d= map(int, input().split())

n = a*d+c*b
m = b*d

_gcd = gcd(m, n)

print(n//_gcd, m//_gcd)