from collections import deque

def solution(picks, minerals):
    
    use = [[1,1,1],[5,1,1],[25,5,1]]
    
    picks_dict = {"diamond" : 0, "iron" : 1, "stone" : 2}
    
    temp = []
    c = 0
    for i in range(0, len(minerals), 5):
        c += 1
        temp.append(minerals[i:i+5])
        if c == sum(picks):
            break
    
    answer = 0
    
    q = deque(temp)
    
    fatigue = []
    
    while q:
        mnrs = q.popleft()
        
        usedDia, usedIron, usedStone = 0, 0, 0
        
        for mnr in mnrs:
            usedDia += use[0][picks_dict[mnr]]
            usedIron += use[1][picks_dict[mnr]]
            usedStone += use[2][picks_dict[mnr]]
            
        fatigue.append([usedDia, usedIron, usedStone])        
    
    fatigue.sort(key = lambda x : (x[2], x[1], x[0]))
    
    for idx, p in enumerate(picks):
        for _ in range(p):
            if fatigue:
                answer += fatigue.pop()[idx]
    
    return answer