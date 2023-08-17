import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

route = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = list(map(int, input().split()))

    route[A].append([B, C])
    route[B].append([A, C])

# 최소 경로 찾기
def dijkstra():
    distances = [10**9] * (N + 1)

    # 레벨, 위치
    heap = [(0, 1)]
    distances[1] = 0

    while heap:

        level, curr = heapq.heappop(heap)

        if curr == N:
            continue

        if distances[curr] < level:
            continue

        for posi, new_level in route[curr]:
            # 경로 중 최대 level을 업데이트
            max_level = max(new_level, level)
            if max_level < distances[posi]:
                distances[posi] = max_level
                heapq.heappush(heap, (max_level, posi))

    return distances[N]

answer = dijkstra()

# 소수 찾기
for i in range(answer+1, 2*answer):
    isPrime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
        break