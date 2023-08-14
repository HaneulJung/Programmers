import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

c2n = {"A" : 0, "B" : 1, "C" : 2, "D" : 3}

queue_list = [deque() for _ in range(4)]

for i in range(N):
    t, p = input().split()
    t = int(t)

    queue_list[c2n[p]].append([i, t])

answer = [-1] * N
is_waiting = [0, 0, 0, 0]
current_time = -1
while queue_list[0] or queue_list[1] or queue_list[2] or queue_list[3]:
    min_time = 10**9
    for i in range(4):
        if queue_list[i]:
            time = queue_list[i][0][1]
            min_time = min(min_time, time)
            if time <= current_time:
                is_waiting[i] = 1

    is_waiting_cnt = sum(is_waiting)

    if is_waiting_cnt == 4:
        break
    
    if is_waiting_cnt == 0:
        current_time = min_time
        continue

    for i in range(4):
        if is_waiting[i] and not is_waiting[(i - 1) % 4]:
            idx, _ = queue_list[i].popleft()
            answer[idx] = current_time

    is_waiting = [0, 0, 0, 0]

    current_time += 1

for ans in answer:
    print(ans)