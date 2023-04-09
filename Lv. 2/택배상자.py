from collections import deque

def solution(order):
    answer = 0
    
    assist = []
    order = deque(order)
    
    l = len(order)
    
    idx = 1
    while order:   
        if assist and assist[-1] == order[0]:
            assist.pop()
            order.popleft()
            answer += 1
            continue
            
        if order[0] == idx:
            order.popleft()
            answer += 1
        else:
            assist.append(idx)
        idx += 1
        
        if idx > l + 1:
            break
    
    return answer