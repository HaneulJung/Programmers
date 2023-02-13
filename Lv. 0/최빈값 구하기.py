def solution(array):
    answer = 0
    
    count_list = []
    m = 1
    for i in set(array):
        count_list.append(array.count(i))
        
        if array.count(i) >= m:
            m = array.count(i)
            answer = i
    if count_list.count(m) > 1:
        return -1
    
    return answer