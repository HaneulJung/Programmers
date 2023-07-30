from collections import deque

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    ss = sum(queue1) + sum(queue2)
    
    if ss % 2 == 1:
        return -1
    
    halfSum = ss / 2
    
    answer = 0
    
    s = sum(queue1)
    c = 0
    l = len(queue1)
    while queue1 and queue2 and c < l * 3:
        if s > halfSum:
            a = queue1.popleft()
            s -= a
            queue2.append(a)
            answer += 1
        elif s < halfSum:
            a = queue2.popleft()
            s += a
            queue1.append(a)
            answer += 1
        else:
            return answer
        c += 1
        
    return -1