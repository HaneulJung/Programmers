def solution(topping):
    answer = 0
    
    older = set()
    younger = {}
    
    for t in topping:
        if t not in younger.keys():
            younger[t] = 1
        else:
            younger[t] += 1
    
    for t in topping:
        older.add(t)
        younger[t] -= 1
        
        if younger[t] == 0:
            del younger[t]
        
        if len(older) == len(younger):
            answer += 1
    
    return answer