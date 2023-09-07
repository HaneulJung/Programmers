def solution(triangle):
    answer = [[0]*i for i in range(1, len(triangle)+1)]    
    answer[0][0] = triangle[0][0]
        
    for i in range(1, len(triangle)):
        answer[i][0] = answer[i-1][0] + triangle[i][0]
        answer[i][-1] = answer[i-1][-1] + triangle[i][-1]
        
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i])-1):
            answer[i][j] = max(answer[i-1][j-1], answer[i-1][j]) + triangle[i][j]
                  
    return max(answer[-1])