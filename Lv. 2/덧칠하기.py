from collections import deque

def solution(n, m, section):
    answer = 0
    
    q = deque(section)
    
    while q:
        i = q.popleft()
        while len(q) != 0 and q[0] <= i + m - 1:
            q.popleft()
        answer += 1
    return answer