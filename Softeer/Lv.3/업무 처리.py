import sys
from collections import deque

input = sys.stdin.readline

H, K, R = map(int, input().split())

cur_work = [deque() for _ in range(2**(H+1))]

for i in range(2**H, 2**(H+1)):
    cur_work[i] = deque(list(map(int, input().split())))

cnt = 0
for time in range(0, R):
    if cur_work[1]:
        cnt += cur_work[1].popleft()

    for i in range(1, 2**H):
        if time % 2 == 0:   # 짝수 날, 오른쪽에서 가져오기
            if cur_work[2*i+1]:
                cur_work[i].append(cur_work[2*i+1].popleft())
        else:               # 홀수 날, 왼쪽에서 가져오기
            if cur_work[2*i]:
                cur_work[i].append(cur_work[2*i].popleft())

print(cnt)