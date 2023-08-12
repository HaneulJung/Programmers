import sys
from collections import deque
from pprint import pprint

go_left = (0,-1)
go_right = (0,1)
go_up = (-1,0)
go_down = (1,0)

# 진입 방향 1 : 왼->오, 2 : 아래 -> 위, 3 : 오->왼, 0 : 위->아래, 신호 % 4 값 이용
signals = {
    1: [go_up, go_right, go_down],      # 진입 방향 : 1
    2: [go_left, go_up, go_right],      # 진입 방향 : 2
    3: [go_down, go_left, go_up],       # 진입 방향 : 3
    4: [go_left, go_down, go_right],    # 진입 방향 : 0
    5: [go_up, go_right],               # 진입 방향 : 1
    6: [go_left, go_up],                # 진입 방향 : 2
    7: [go_left, go_down],              # 진입 방향 : 3
    8: [go_down, go_right],             # 진입 방향 : 0
    9: [go_right, go_down],             # 진입 방향 : 1
    10: [go_up, go_right],              # 진입 방향 : 2
    11: [go_left, go_up],               # 진입 방향 : 3
    12: [go_left, go_down]              # 진입 방향 : 0
}

def check_fromWhere(signal):
    if signal == go_left:
        return 3
    elif signal == go_right:
        return 1
    elif signal == go_up:
        return 2
    else:
        return 0

input = sys.stdin.readline

N, T = map(int, input().split())

intersections = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        intersections[i][j] = list(map(int, input().split()))

queue = deque()
queue.append([1, 1, 0, 2]) # y 좌표, x 좌표, t 시간, 진입방향

answer = set()
while queue:
    y, x, t, i = queue.popleft()
    answer.add((y, x))
    if i == intersections[y][x][t%4] % 4:  # 진입 방향 맞는지 확인
        for signal in signals[intersections[y][x][t%4]]:  
            dy = y + signal[0]
            dx = x + signal[1]
            if (1 <= dy <= N) and (1 <= dx <= N) and t < T:
                queue.append([dy, dx, t+1, check_fromWhere(signal)])

print(len(answer))