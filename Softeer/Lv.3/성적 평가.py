import sys
import heapq

input = sys.stdin.readline

N = int(input())

final_score = [0] * N

for _ in range(3):
    scores = list(map(int, input().split()))

    tmp = []
    order = {}
    answer = [0] * N

    for i in range(N):
        final_score[i] += scores[i]
        
        if -scores[i] not in tmp:
            heapq.heappush(tmp, -scores[i])

        if scores[i] not in order.keys():
            order[scores[i]] = []
        order[scores[i]].append(i)

    rank = 1
    while tmp:
        val = -heapq.heappop(tmp)
        cnt = 0
        for i in order[val]:
            answer[i] = rank
            cnt += 1
        rank += cnt
    
    for i in range(N):
        print(answer[i], end=" ")
    print("")

tmp = []
order = {}
answer = [0] * N
for i in range(N):
    if -final_score[i] not in tmp:
        heapq.heappush(tmp, -final_score[i])

    if final_score[i] not in order.keys():
        order[final_score[i]] = []
    order[final_score[i]].append(i)

rank = 1
while tmp:
    val = -heapq.heappop(tmp)
    cnt = 0
    for i in order[val]:
        answer[i] = rank
        cnt += 1
    rank += cnt

for i in range(N):
    print(answer[i], end=" ")