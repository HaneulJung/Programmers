import sys
import heapq

N = int(sys.stdin.readline())

lectures = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(lectures, (e,s))

cnt = 0
end_time = 0

while lectures:
    e, s = heapq.heappop(lectures)
    if s >= end_time:
        now = e
        cnt += 1

print(cnt)