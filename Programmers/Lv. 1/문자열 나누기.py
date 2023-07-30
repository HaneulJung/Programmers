def solution(s):
    answer = 0
    dic = {"x":0, "nx":0}    
    set = False
    temp = ''
    
    for ss in s:
        if not set:
            set = True
            temp = ss
            
        if ss == temp:
            dic["x"] += 1
        else:
            dic["nx"] += 1
        
        if dic["x"] == dic["nx"]:
            answer += 1
            dic = {"x":0, "nx":0}
            set = False
    
    if dic["x"] != 0:
        answer += 1
        
    return answer