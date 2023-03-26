def solution(n):
    answer = []
    
    temp = [[0] * n for _ in range(n)]
    
    hor, ver, num = 0, -1, 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                ver += 1
            elif i % 3 == 1:
                hor += 1
            else:
                hor -= 1
                ver -= 1
            
            temp[ver][hor] = num
            num += 1
            
    for i in range(n):
        for j in range(n):
            if temp[i][j] != 0:
                answer.append(temp[i][j])
    
    return answer