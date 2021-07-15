import sys

N, K = map(int, sys.stdin.readline().split())
N = [int(i) for i in str(N)]
length_N  = len(N)

if length_N == 1:
    print(-1)
    sys.exit()
if length_N == 2 and N[1] == 0:
    print(-1)
    sys.exit()

max_N = sorted(N, reverse=True)
result = []


def change(arr, x, y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp
    return arr


def ConvertToInt(arr):
    res = ''
    for i in arr:
        res += str(i)
    return int(res)


def dfs(depth, arr):
    if depth == K:
        result.append(ConvertToInt(arr))
        return

    index = -1
    for i in range(length_N):
        if arr[i] != max_N[i]:
            index = i
            break
    if index == -1:
        if length_N != len(set(arr)):
            print(ConvertToInt(arr))
            sys.exit()
        else:
            arr = change(arr, length_N-2, length_N-1)
            dfs(depth+1, arr)
            return
    else:
        tmp_index = []
        for i in range(index+1, length_N):
            if max_N[index] == arr[i]:
                tmp_index.append(i)

        for i in tmp_index:
            arr1 = list(map(int, arr))
            dfs(depth+1, change(arr1, index, i))


dfs(0, N)

max_result = 0
for i in result:
    if i > max_result:
        max_result = i
print(max_result)