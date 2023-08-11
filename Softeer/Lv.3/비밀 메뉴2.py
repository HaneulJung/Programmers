import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

first = list(map(str, input().split()))
second = list(map(str, input().split()))

C = [[0] * M for _ in range(N)]

max_len = 0
for i in range(N):
    for j in range(M):
        if first[i] == second[j]:
            if i == 0 or j == 0:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + 1
        max_len = max(max_len, C[i][j])

print(max_len)