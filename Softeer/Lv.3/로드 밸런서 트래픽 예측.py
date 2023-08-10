import sys
from collections import deque

input = sys.stdin.readline

# N: 서버 개수, K: 요청 개수
N, K = map(int, input().split())

# line: 간선
line = []
for _ in range(N):
    line.append(list(map(int, input().split())))

# 들어오는 선 수
inline = [0] * N
for i in range(N):
    if len(line[i]) > 1:
        for j in line[i][1:]:
            inline[j-1] += 1

# topology_sort
topology_sort = []
queue = deque()
queue.append(0)

while queue:
    now = queue.popleft()
    topology_sort.append(now)
    for i in line[now][1:]:
        inline[i-1] -= 1
        if inline[i-1] == 0:
            queue.append(i-1)    

# 트래픽 분배
traffic = [0] * N
traffic[0] = K
for ts in topology_sort:
    if len(line[ts]) > 1:
        t, arr = line[ts][0], line[ts][1:]

        moc = traffic[ts] // t
        nam = traffic[ts] % t

        for i in arr:
            traffic[i-1] += moc

        for i in range(nam):
            traffic[arr[i]-1] += 1

for t in traffic:
    print(t, end=" ")