def solution(num, k):    
    for i in range(len(str(num))):        
        if (int(str(num)[i]) == k):
            return i + 1
    return -1