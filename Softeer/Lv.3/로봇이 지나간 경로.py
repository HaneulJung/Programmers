import sys
from collections import deque
from pprint import pprint
import copy

input = sys.stdin.readline

H, W = map(int, input().split())

maps = []
for _ in range(H):
    maps.append(list(input().strip()))

checks = [(-1,0), (0,1), (1,0), (0,-1)]
directions = ['^', ">", "v", "<"]

for y in range(H):
    for x in range(W):
        cnt = 0
        if maps[y][x] == '#':
            for i in range(4):
                ny = y + checks[i][0]
                nx = x + checks[i][1]
                if 0 <= ny < H and 0 <= nx < W and maps[ny][nx] == '#':
                    direction = i
                    cnt += 1

            if cnt == 1:
                start_point = [y, x, direction]
                break

queue = deque()
queue.append(start_point)   # h, w 좌표, pre_dir

print(f'{start_point[0]+1} {start_point[1]+1}\n{directions[start_point[2]]}')

cmd = ''

while queue:
    th, tw, pre_dir = queue.popleft()
    for i in range(4):
        dh1 = th + checks[i][0]
        dw1 = tw + checks[i][1]
        dh2 = th + checks[i][0]*2
        dw2 = tw + checks[i][1]*2
        if (0 <= dh2 < H) and (0 <= dw2 < W) and maps[dh1][dw1] == '#' and maps[dh2][dw2] == '#':
            maps[dh1][dw1] = '.'
            maps[dh2][dw2] = '.'

            if pre_dir == i:    
                cmd += "A"
            elif (pre_dir + 1) % 4 == i :
                cmd += "RA"
            elif (pre_dir - 1) % 4 == i:
                cmd += "LA"

            queue.append([dh2, dw2, i])

print(cmd)