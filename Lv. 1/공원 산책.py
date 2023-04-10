def solution(park, routes):
    move = {"E" : (0,1), "W" : (0,-1), "S" : (1,0), "N" : (-1,0)}
    
    start_point = (0,0)
    
    height = len(park)
    width =  len(park[0])
    
    for i in range(height):
        for j in range(width):
            if park[i][j] == "S":
                start_point = (i, j)    
    
    cur_h, cur_w = start_point[0], start_point[1]                    
    
    for route in routes:
        direction, distance = route.split(" ")[0], int(route.split(" ")[1])   
        
        if cur_h + move[direction][0] * distance > height - 1 or \
            cur_h + move[direction][0] * distance < 0 or \
            cur_w + move[direction][1] * distance > width - 1 or \
            cur_w + move[direction][1] * distance < 0:
            continue
            
        isObtacle = False
        for d in range(1,distance+1):
            if park[cur_h + move[direction][0] * d][cur_w + move[direction][1]*d] == "X":
                isObtacle = True
                break
        
            
        if not isObtacle:
            cur_h += move[direction][0] * distance
            cur_w += move[direction][1] * distance        
        
    return [cur_h, cur_w]