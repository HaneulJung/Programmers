import sys
from collections import deque

N = int(sys.stdin.readline())

maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip())))

move = [[1,0],[0,1],[-1,0],[0,-1]]

visited = [[False] * N for _ in range(N)]

answer = []
for y in range(N):
    for x in range(N):
        if not visited[y][x] and maps[y][x]: 
            queue = deque()
            queue.append([y,x])
            visited[y][x] = True
            cnt = 1
            while queue:
                q = queue.popleft()
                ty, tx = q[0], q[1]
                for i in range(4):
                    dy = ty + move[i][0]
                    dx = tx + move[i][1]
                    if (0 <= dy < N and 0 <= dx < N) and maps[dy][dx] and not visited[dy][dx]:
                        visited[dy][dx] = True
                        queue.append([dy,dx])
                        cnt += 1
            answer.append(cnt)
            
print(len(answer))
for c in sorted(answer):
    print(c)