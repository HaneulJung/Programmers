def solution(board):
    n = len(board)
    
    answer = 0

    isDangerous = False
    
    for i in range(0,n):
        for j in range(0,n):
            isDangerous = False
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    if i + a >= 0 and i + a < n and j + b >= 0 and j + b < n and board[i+a][j+b] == 1: 
                        print(i, j, a, b)
                        isDangerous = True
                        break
                if (isDangerous):
                    answer += 1
                    break
    return n*n - answer