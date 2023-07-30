def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key= lambda x : (x[col-1], -x[0]))
    
    S = []
    
    for r in range(row_begin-1, row_end):
        temp = 0
        for d in data[r]:
            temp += d % (r+1)
        S.append(temp) 
        
    for s in S:
        answer = answer ^ s
        
    return answer