def solution(array, n):
    array.append(n)
    array.sort()
    
    c = array.index(n)
    
    if (c == 0):
        return array[c+1] 
    
    if (c == len(array)-1):
        return array[c-1]
    
    if (n - array[c-1] > array[c+1] - n):
        return array[c+1] 
    else:
        return array[c-1]