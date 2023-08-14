import sys
import copy

input = sys.stdin.readline

N = int(input())

buses = [0] + list(map(int, input().split()))

arr = [[0] * (N+1) for _ in range(N+1)]
for x in range(1, N+1):
    arr[x][N] = 0
    arr[x][N-1] = 1 if (buses[N] < x) else 0
    for j in range(N-2, 0, -1):
        if (buses[j+1] < x):
            arr[x][j] = arr[x][j+1] + 1
        else:
            arr[x][j] = arr[x][j+1]

cnt = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if buses[i] < buses[j]:
            cnt += arr[buses[i]][j]

print(cnt)