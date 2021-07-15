n = int(input())
idx = 2
r = int(n ** 0.5)

while idx <= r:
    while not n % idx:
        print(idx)
        n //= idx
    idx += 1
if n > 1:
    print(n)