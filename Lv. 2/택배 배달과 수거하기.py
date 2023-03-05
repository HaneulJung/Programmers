def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:   
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        
        while pickups and pickups[-1] == 0:
            pickups.pop()
            
        c = max(len(deliveries), len(pickups))        
        answer += (c * 2)  
        
        d = cap
        p = cap
        
        while d != 0 and deliveries:
            if deliveries[-1] == 0:
                deliveries.pop()
                continue
                
            if d >= deliveries[-1]:
                d -= deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= d
                d = 0
        
        while p != 0 and pickups:
            if pickups[-1] == 0:
                pickups.pop()
                continue
                
            if p >= pickups[-1]:
                p -= pickups[-1]
                pickups.pop()
            else:
                pickups[-1] -= p
                p = 0                       
            
    return answer




def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    d = 0
    p = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer