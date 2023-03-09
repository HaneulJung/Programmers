def solution(dirs):
    answer = 0
    
    move = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    
    visited = {}
    
    px, py = 0, 0
    for dir in dirs:
        if px + move[dir][0] < -5 or px + move[dir][0] > 5 or \
            py + move[dir][1] < -5 or py + move[dir][1] > 5:
            continue
            
        cx = px + move[dir][0]
        cy = py + move[dir][1]
        
        if sorted([(px, py), (cx, cy)]) not in visited.values():
            visited[answer] = sorted([(px, py), (cx, cy)])
            answer += 1
        
        px = cx
        py = cy
        
    return answer