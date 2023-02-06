def solution(lines):
    dict = {}
    for i in range(-100, 100):
        dict[i] = 0
        
    for line in lines:
        for i in range(line[0], line[1]):
            dict[i] += 1
    
    count = 0
    for v in dict.values():
        if v > 1:
            count += 1
    
    return count