import sys
from collections import deque

# N 세로, M 가로
N, M = map(int, sys.stdin.readline().split())

ice = []
for _ in range(N):
    ice.append(list(map(int, sys.stdin.readline().split())))

checks = [(1,0), (-1,0), (0,1), (0,-1)]

def isEmpty(arr):
    for i in range(len(arr)):
        if sum(arr[i]) != 0:
            return False
    return True

time_elapsed = 0
while not isEmpty(ice):    
    queue = deque()
    queue.append([0,0])    
    
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    # 지워질 얼음 찾기
    while queue:
        y, x = queue.popleft()
        for check in checks:
            dy = y + check[0]
            dx = x + check[1]
            if (0 <= dy < N) and (0 <= dx < M):
                if ice[dy][dx] == 1:
                    visited[dy][dx] += 1
                
                if visited[dy][dx] == 0:
                    queue.append([dy,dx])
                    visited[dy][dx] = 1
 
    # 얼음 삭제
    for y in range(N):
        for x in range(M):
            if visited[y][x] > 1:
                ice[y][x] = 0

    time_elapsed += 1

print(time_elapsed)