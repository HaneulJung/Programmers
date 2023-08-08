import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

maps = []
for _ in range(R):
    maps.append(list(sys.stdin.readline().strip()))

checks = [(1,0), (-1,0), (0,1), (0,-1)]


# 소나기 확산
def expand_rain(tmp_map):
    rains = []
    for r in range(R):
        for c in range(C):
            if tmp_map[r][c] == '*':
                rains.append([r,c])
    for rain in rains:
        for check in checks:
            tr = rain[0] + check[0]
            tc = rain[1] + check[1]
            if (0 <= tr < R) and (0 <= tc < C) and tmp_map[tr][tc] == '.':
                tmp_map[tr][tc] = '*'
    return tmp_map

# 출발지점 찾기
def find_W():
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'W':
                return [r, c]

start_r, start_c = find_W()

    
queue = deque()
queue.append([start_r, start_c, 0])
visited = [[0] * C for _ in range(R)]
visited[start_r][start_c] = 1
maps = expand_rain(maps)
temp = 0

answer = 0
while queue:
    r, c, idx = queue.popleft()
    if temp != idx: # 시간이 증가 할때만 소나기가 확산되도록 만듬 
        maps = expand_rain(maps)
    temp = idx 
    for check in checks:
        tr = r + check[0]
        tc = c + check[1]
        if (0 <= tr < R) and (0 <= tc < C) and not visited[tr][tc]:
            visited[tr][tc] = 1
            if maps[tr][tc] == '.':     
                queue.append([tr, tc, idx+1])
            elif maps[tr][tc] == 'H':                
                answer = idx + 1
                break

if answer:
    print(answer)
else:
    print('FAIL')