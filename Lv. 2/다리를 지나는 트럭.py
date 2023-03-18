from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque(truck_weights)
    
    ship = deque([q.popleft()])
    length = deque([0])
    
    while ship or q:
        for i in range(len(length)):
            length[i] += 1
        if length[0] == bridge_length:
            ship.popleft()
            length.popleft()
            
        if len(q) != 0:
            if sum(ship) + q[0] <= weight:
                ship.append(q.popleft())
                length.append(0)        
        
        answer += 1
    
    return answer + 1