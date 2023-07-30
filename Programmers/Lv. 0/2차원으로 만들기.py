def solution(num_list, n):
    answer = []
    temp = []
    
    for num in num_list:
        temp.append(num)
        if len(temp) == n:
            answer.append(temp)
            temp = []
    
    
    return answer