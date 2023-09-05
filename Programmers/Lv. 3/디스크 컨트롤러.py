import heapq

def solution(jobs):
    answer = 0

    workHeap = []

    jobs.sort(key=lambda x : x[0]) 

    start, now = -1, 0
    idx = 0
    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(workHeap, (job[1], job[0]))

        if workHeap:
            workTime, requestTime = heapq.heappop(workHeap)
            start = now
            now += workTime
            answer += now - requestTime
            idx += 1
        else:
            now += 1

    return answer // len(jobs)