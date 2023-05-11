def solution(k, ranges):
    answer = []
    
    areas = []
    axis_y = [k]
    
    while k > 1:
        if k % 2 == 0:
            k = k / 2
        else:
            k = k * 3 + 1            
        
        areas.append((axis_y[-1] + k) / 2)
        axis_y.append(k)
    
    for r in ranges:
        if r[0] - r[1] == len(areas):
            answer.append(0.0)
        elif r[0] - r[1] > len(areas):
            answer.append(-1.0)
        else:
            answer.append(sum(areas[r[0]:len(areas)+r[1]]))
    
    
    return answer