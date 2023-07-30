def solution(name, yearning, photo):
    answer = []
    
    dict = {}
    
    for i in range(len(name)):        
        dict[name[i]] = yearning[i]
    
    for pt in photo:
        s = 0
        for p in pt:
            if p in dict.keys():
                s += dict[p]
        answer.append(s)
    
    return answer