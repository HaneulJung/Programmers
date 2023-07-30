def solution(sequence, k):
    
    n = len(sequence)
    
    answer = []
    
    idx = 0
    s = 0
        
    for i in range(n):
        while s < k and idx < n:
            s += sequence[idx]
            idx += 1
            
        if s == k:
            answer.append([i, idx-1])
            
        s -= sequence[i]     
        
    return sorted(answer, key = lambda x : (x[1] - x[0]))[0]