import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())

maps = []
for _ in range(H):
    maps.append(list(map(int, sys.stdin.readline().split())))

cmds = []
Q = int(sys.stdin.readline())
for _ in range(Q):
    i, j, c = map(int, sys.stdin.readline().split())
    cmds.append([i-1, j-1, c])

checks = [(1,0), (-1,0), (0,1), (0,-1)]

for cmd in cmds:
    i, j, c = cmd

    number = maps[i][j]
    maps[i][j] = c

    queue = deque()
    queue.append([i,j])

    visited = [[False] * W for _ in range(H)]
    visited[i][j] = True

    while queue:
        ti, tj = queue.popleft()
        for check in checks:
            di = ti + check[0]
            dj = tj + check[1]
            if (0 <= di < H) and (0 <= dj < W) and not visited[di][dj] and maps[di][dj] == number:
                visited[di][dj] = True
                maps[di][dj] = c
                queue.append([di, dj])

for i in range(H):
    for j in range(W):
        print(maps[i][j], end=" ")
    print()