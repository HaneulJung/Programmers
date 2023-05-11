from heapq import heappush, heappop

def solution(n, k, enemy):
    hq = []
    
    for i, e in enumerate(enemy):
        heappush(hq, e)
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return i
        
    return len(enemy)