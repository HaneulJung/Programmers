def solution(want, number, discount):
    answer = 0
    
    l = len(discount)
    
    for i in range(l - 9):
        no = False
        d = discount[i:i+10]
        for w in range(len(want)):
            if d.count(want[w]) != number[w]:
                no = True      
                break
        if not no:
            answer += 1       
        
    return answer